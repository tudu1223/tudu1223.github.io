---
title: 'HANDS ON LLM'
summary: '从 tokenizer 到评测到生物学落地的 LLM 实战笔记 —— tokenization / 预训练 / 对齐 / 推理 / 评测 / 单细胞下游,一份给"想做点事"的本科生整理的小抄。'
date: '2026-01-15'
authors:
  - sky-huang
tags:
  - Research Notes
  - LLM
  - Hands-on
categories:
  - research-notes
---

# HANDS ON LLM

> 这不是教程,是一份**给生物/AI 跨学科方向本科生的 LLM 实战路线笔记**。
> 假设你已经跑通过一个最小训练循环(类似 PyTorch 的 MNIST),想搞清楚"LLM 和我以前跑的那个 ResNet 到底什么区别"。每个章节都尽量能在 30 分钟内动手复现一份。

## 0. 路线图

我把整条路线拆成 **6 层**:

```
0. PyTorch 基础循环                    ← 起步:已经会
1. Tokenization (BPE / SentencePiece)  ← "文本怎么变向量"
2. 预训练 (decoder-only LM)             ← "为什么叫 next-token prediction"
3. 后训练: SFT / DPO / RLHF            ← "为什么有了 base 还要 align"
4. 推理: KV cache / speculative        ← "为什么 7B 模型 4090 能跑"
5. 评测: MMLU / GSM8K / 长文本         ← "怎么知道一个模型'好不好'"
6. 下游: 单细胞 / GRN 等               ← "和我的方向怎么连"
```

下面每一层都给出**最小代码 + 我自己踩过的坑**。

---

## 1. Tokenization:文本怎么变成向量

**直觉**:模型不认识字,只认识 token id。Tokenizer 负责把人话切成 token,再映射成整数。

```python
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
ids = tok.encode("单细胞转录组学", return_tensors="pt")  # 长这样 shape: [1, 7]
print(tok.convert_ids_to_tokens(ids[0]))
# ['单', '细胞', '转', '录', '组', '学']
```

**关键事实**(我踩过):

1. **中文基本用 BPE 拆字**,英文按词片段。Qwen/Baichua 这类中文模型把"单细胞"切成两个字,而不是当成一个词 — 因为训练语料里"单细胞"出现频率不够凑成一个 token。
2. **词表大小 ≠ 模型能力**。词表越大,平均序列越短但每 token 的信息量越稀。一般 32K-128K 是当代 sweet spot。
3. **`encode` 加 `encode_plus` 还是 `tokenizer(...)`?** 三者返回不一样。直接用 `tokenizer(text, return_tensors="pt")` 最稳,会自动加 BOS/EOS。

**动手建议**:跑 `tokenizer.convert_ids_to_tokens(...)` 把模型 vocab 里 30 个高频 token 打印出来,看看模型是怎么切你的中文输入的。

---

## 2. 预训练:decoder-only LM 与 next-token prediction

**直觉**:decoder-only LM 就是"给定前 N 个 token,预测第 N+1 个 token",然后无限循环。loss 是 cross-entropy。没有别的 trick,只是把 loss 算得足够多次。

```python
import torch, torch.nn.functional as F
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct", torch_dtype=torch.bfloat16)
input_ids = tok("单细胞", return_tensors="pt").input_ids
out = model(input_ids)
logits = out.logits  # [1, 2, vocab_size]

# next-token loss:
shift_logits = logits[:, :-1, :].contiguous()
shift_labels = input_ids[:, 1:].contiguous()
loss = F.cross_entropy(
    shift_logits.view(-1, shift_logits.size(-1)),
    shift_labels.view(-1),
)
loss.backward()
```

**几个非显然的事实**:

1. **位置编码现在已经几乎全是 RoPE**(GPT-NeoX、LLaMA、Qwen、Mistral 全是 RoPE)。原始 transformer 的正弦位置编码在 2024 年之后基本没人用了 — 因为 RoPE 对长度外推天然友好。
2. **预训练 objective 与 SFT objective 是同一种 loss**,只是数据分布不同。所谓"SFT 微调"实际上就是"在特定对话格式上继续做 next-token 预测"。
3. **scale 90% 的 magic 在数据和算力**。架构方面,从 GPT-2 → GPT-4 实质上的改动比传说中少(decoder self-attention + MLP 中间放大 4 倍 + RMSNorm + SwiGLU)。但数据和算力 scale 上去之后的能力跳变是真实的。

**动手建议**:拿 `Qwen2.5-0.5B` 在你自己的单细胞笔记或论文摘要上做 1 epoch 的继续预训练(continue pretraining),看 loss 从 3.x 降到 2.x 需要多少时间,亲身体会一下"scale"。

---

## 3. 后训练:SFT、DPO、RLHF 到底在干什么

**直觉**:预训练出来的 base 模型是个"语言续写机",你需要把它变成助手。这一步叫 **alignment / post-training**。

### 3.1 SFT(Supervised Fine-Tuning)

最朴素 — 在 `(prompt, ideal_response)` 数据上做监督学习。

```python
from trl import SFTTrainer, SFTConfig
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")

trainer = SFTTrainer(
    model=model,
    train_dataset=ds,                       # [{"messages": [...]}]
    args=SFTConfig(
        output_dir="./sft-out",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        learning_rate=2e-5,
        bf16=True,
    ),
    processing_class=tok,
)
trainer.train()
```

### 3.2 DPO(Direct Preference Optimization)

RLHF 难训 — 需要 PPO + reward model + value head + 4 份模型在内存里。DPO(Zhang et al. 2024)直接绕过 reward model,用 `(chosen, rejected)` pair 做 pairwise 训练,效果接近 RLHF 但只用一个模型。

```python
from trl import DPOTrainer, DPOConfig
trainer = DPOTrainer(
    model=model,
    train_dataset=ds,  # [{"prompt":..., "chosen":..., "rejected":...}]
    args=DPOConfig(
        output_dir="./dpo-out",
        beta=0.1,        # KL 强度,越大越接近 base 模型
        num_train_epochs=1,
    ),
)
```

**经验**:DPO 对数据质量极度敏感。1000 条人工标注的 DPO pair 通常比 10 万条自动构造的强。

### 3.3 RLHF(PPO 那一套)

除非你做专门的 alignment 研究,否则**先 SFT 再 DPO** 足够。RLHF 留给真正需要调安全性 / 风格的场景。

---

## 4. 推理:KV cache、量化、speculative decoding

部署一个 7B 模型到 RTX 4090 (24GB):

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

bnb = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-7B-Instruct",
    quantization_config=bnb,
    device_map="auto",
)
```

**几个关键概念**:

1. **KV cache** — 推理时把每层每个 head 的 K/V 矩阵缓存到显存/内存,避免生成第 N+1 个 token 时重算前 N 个。在 chat 这种长对话场景里,KVRAM 通常是显存瓶颈的主要部分。
2. **量化** — 4-bit NF4 把显存压到 ~6GB。代价是 loss 一点点(用 QLoQA 论文的标准 bench 几乎测不出来)。
3. **vLLM / SGLang** — 生产推理引擎,把 KV cache 分页(PagedAttention)用,吞吐量比原生 `model.generate()` 高 10-30 倍。本地开发用 `transformers`,上线换 vLLM。
4. **Speculative decoding** — 用一个小模型先草拟 K 个 token,大模型并行验证。比直接用大模型生成快 2-3 倍。

---

## 5. 评测:别被 leaderboard 蒙了

**LM 评测生态混乱**。MMLU、GSM8K、HellaSwag、TruthfulQA、ARC、HLE(2025 新出的 hard suite)、LiveBench — 各跑各的,不同的 prompt template 同样的模型能差 5 分。

我自己的经验:

```python
from lm_eval import simple_evaluate

results = simple_evaluate(
    model="hf",
    model_args="pretrained=Qwen/Qwen2.5-0.5B-Instruct,dtype=bfloat16",
    tasks=["mmlu_stem", "gsm8k", "hellaswag"],
    batch_size="auto",
)
print(results["results"]["mmlu_stem"]["acc,none"])
```

**几个现实**:

1. **5-shot vs 0-shot vs chain-of-thought** 的差异经常比"两个不同模型"的差异还大。报指标时一定要写清楚。
2. **MMLU 评分和实际科研能力几乎脱钩**。一个 MMLU 70% 的模型在陌生领域写实验代码可能完全不能用。**做 AI4bio 一定要在自己的下游 benchmark 上评估**。
3. **leaderboard 排名的参数和代码不公开**,大部分排名不能复现。这一点跟 [我之前在 BEELINE 上看到的现象是一样的]({{< ref "/blog/ai4bio-turning-point" >}}):

> "Benchmark 不公开代码 = leaderboard 不可信"

---

## 6. 下游:怎么接到我的生物学方向

我目前在做的几件事:

1. **单细胞 foundation model 做 embedding**,用 [scGPT](https://github.com/bowang-lab/scGPT) / [GeneFormer](https://huggingface.co/ctheodoris/GeneFormer) / [scBERT](https://github.com/TencentAILabHealthcare/scBERT) 提取细胞 embedding,然后喂给传统 GRN 推断工具(GENIE3 / GRNBoost2)。
2. **DPO 训练一个能"以湿实验能用的格式"读 single-cell 数据的助手**。原始 count matrix 一上来就让 LLM 看,要么 hallucinate 要么乱说。要在 DPO 数据里**严格格式约束**,比如"只能输出 Ensembl ID 列表"。
3. **评测自己做一个** — 不押 leaderboard,而是看"同样预算下,这个 pipeline 能不能把 BEELINE 复现到 90% 一致"。

---

## 一份参考时长表

如果你每天 1 小时持续投入:

| 阶段 | 时长 | 关键里程碑 |
|---|---|---|
| Tokenization + 跑通最小预训练 | 1 周 | 能手写一个 10M 参数的 decoder LM 训 1 epoch |
| Pretraining 一个 0.5B 模型 | 2-4 周 | 在你自己的语料上 loss 降到合理水平 |
| SFT + DPO | 1-2 周 | 能写出能用的对话 demo |
| 推理 + 量化 + vLLM | 1 周 | 7B 模型在 RTX 4090 上吞吐 ≥30 tok/s |
| 评测 + 自己做下游 bench | 持续 | 你比 leaderboard 更懂你的模型 |

## 一些我不踩但别人会踩的坑

- **别在中文任务上用裸 GPT 系列的 tokenizer** — 中文 token 碎得离谱。
- **别用 AdamW 之外的 optimizer 作为第一步** — Adam 家族稳得多。
- **别用 FP32 训练任何 ≥100M 参数模型** — 半精度(bf16/fp16)是当代默认。
- **别相信任何"模型超越 GPT-4"的博客标题** — 都要自己复现。
- **别把"训练 loss"和"实际能力改善"画等号** — 训练 loss 是必要不充分。

---

## 下一步

下一篇 **[CS231n 学习笔记](/blog/cs231n-notes/)** 我把视觉模型那一套对齐过来 — CNN/ResNet/ViT 与 Transformer decoder 的同构性是我从这个课里拿到的最大启发。

具体到 AI4bio 的一篇深度稿,我把它单独写成了 **[AI4bio 转折点:leaderboard 不是终点,湿实验才是](/blog/ai4bio-turning-point/)** — 跟这份 LLM 笔记互为补充。
