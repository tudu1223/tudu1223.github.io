---
title: 'AI4bio at a turning point: why I bet on wet-lab pipelines over leaderboards'
summary: '反思类深度稿:站在 AI4bio 转折点,论证"押 leaderboard 等于押错方向",提出 wet-lab-actionable pipeline 的具体路径 —— apples-to-apples BEELINE 复现 + 可复现 CPU 基线。本科起步的研究立场说明。'
date: '2026-02-01'
authors:
  - sky-huang
tags:
  - Research Notes
  - AI4Science
  - GRN inference
  - Opinion
  - Method Notes
categories:
  - research-notes
---

> 这是一篇**反思类**稿,不是一个 survey。它不是要穷尽所有 AI4bio 的方向,而是想清楚**我选择押哪条路、为什么不押另一条、凭什么这个判断也许不是错的**。如果你来我的方向(单细胞 GRN 推断),这篇文章会给你我的路线图;如果你不在这个方向,它大致仍然适用 —— 同样的"leaderboard vs 湿实验"张力,在几乎所有 AI4bio 子领域都成立。

## TL;DR

1. AI4bio 已经来到一个转折点:**模型能力早期阶段已经过了,评测文化还在早期**。
2. 我押的方向:**先写一个能跑、可复现、不需要 GPU cluster 也能复现的管道**,然后贴着 BEELINE 这类公开 benchmark 做"apples-to-apples"。不是 top leaderboard,但能证明哪些 leaderboard 排名的差距是真的、哪些是评测脚本自己的浮动。
3. 我**不押**的方向:堆更大参数、刷单一 benchmark、追求一项 reporting 的 SOTA 来发表。原因写在下面。
4. 这是一份**本科起步的取舍说明**,不是"我已经有结果"的终局论文。如果你也在早期阶段,这是我建议你同步成立的几个立场。

---

## 一、转折点到底指什么

"AI4bio 转折点"是一个比较浮夸的表述。我用它的意思是:**从"AI 能做点生物"过渡到"AI 在生物里能稳定做点什么"**。区别有两点:

- "能做点" = 模型在 toy task 上表现合理
- "稳定做点什么" = 模型在数据集 / 实验室之间**可复现**地做对同一件事

当代的 foundation model 在文本 / 视觉上已经有了后者的样子 —— GPT-4 / Claude / Gemini 在常见 benchmark 上的得分是稳定的,但**单细胞 foundation model (scGPT、GeneFormer、scBERT) 在不同 scRNA-seq 数据集之间的方差非常大**。这个事情不是 model size 解决了的,是评测基础设施的事情。

### 一个具体的例子:BEELINE 上的 leaderboard

BEELINE (Pratapa et al. 2020, *Nature Methods*) 是单细胞基因调控网络 (Gene Regulatory Network, GRN) 推断的标杆 benchmark。它评估 GENIE3 / GRNBoost2 / PIDC / SCENIC 等十几种方法,在四种人造基准 (CNA / mESC / hESC / hHep) 上,以及真实的 BEELINE 评估流水线 (EPR、BER、AUPR、AUC) 上对比。

看上去很扎实。但当你真的去复现时会发现:

1. **预处理与论文不同**。你下到的 Python 包和原论文报告时用的是同一个版本?很多 SCENIC workflow 里 Loom → AnnData 的中间步骤,不同时间点跑出来的指标会差 5-10 个绝对百分点。
2. **超参差异**。GENIE3 默认 maxgenes 在不同 BEELINE 子实验里是不同的 —— 15、50、100,看你用哪个。
3. **数据过滤**。BEELINE 给的 TF list 来源是外部 GTEx / DoRothEA,有些方法用了不同的 list 就跑出另一个顺序。
4. **指标的数值含义**。BER(Best Effort Rate)的"best"是按 average 还是 per-edge,不同代码一致就不错。
5. **评估代码本身的随机性**。即使 seed 锁死,某些 metric 的实现(Numba、cuML、PyTorch)各自的非决定性也让跨平台比较变得微妙。

这意味着 BEELINE leaderboard 上的"Ranking 1 / 2 / 3"在不同的"我自己的预处理 + 我的 TF list + 我自己的 seed"下可能 shuffle。

**我不是说 BEELINE 不行** —— 它是当下最好的,不完美的工作没有好的工作能替代。我说的是:用 BEELINE 的方法排名做最终决策之前,要再做自己的 apples-to-apples。这件事不需要新想法,需要工程。

---

## 二、为什么不押"更大模型"

有一派思路(过去两年最显眼)是:既然 BERT、GPT、ViT、scGPT 都"先 scale 再 finetune",那 GRN 推断是不是也要把这个路径走一遍?这个判断不显然错,但有几个理由我不直接走它。

### 2.1 数据规模本身在生物学里受限

LLaMA-3 在 15T tokens 上预训练。scRNA-seq 的公开 corpus,CellXGene 大概 [~50M cells](https://cellxgene.cziscience.com/),足够 fine-tune 但相对 text corpus 极小。scaling law 不是不能跑 —— 但起点很低,需要 biology-native 的 token scheme (gene panel masking? pathway-level smoothing?) 的工程量级与做 NLP 同等。

### 2.2 评测的复杂度比文本高

文本里"一个句子是否流畅"是相对清晰的任务;GRN 推断里"一个调控边 T → G 是不是真的存在"本质是个未对齐的监督问题(causal biology ≠ correlation 在 bulk 里),大多数数据集只有 ground-truth 不完整的子集。这就让一个更大的模型在同一个 benchmark 上更可能"拟合评测"而不"接近真理"。

### 2.3 资源开销与本科起步的错配

LLaMA-3 70B fine-tune 在学术集群上跑一次要几十万美元 / 几万 GPU 小时。本科起步的研究者显然不在这个层级。这意味着"押 scale"在起步阶段实际上等于不押 —— 资源不在手上,只能做 super-network 的下游。这没错,但只是某一个支线工作。

---

## 三、押什么:wet-lab actionable pipeline

我押的是**"pipeline-level"**的东西,从三个具体方向:

### 3.1 Apples-to-apples BEELINE 复现

把 BEELINE 的 NA / mESC / hESC / hHep benchmark **重新写一遍**,并通过修改三个维度:

1. **预处理对齐** —— 同样的 QC / normalization / HVGs 选法,在所有方法中固定。
2. **超参对齐** —— 每个方法跑 3 个超参集合,取 median 报告。
3. **榜单维度对齐** —— 每个方法除了 BEELINE 的四个指标,加 自己加的"扰动鲁棒性"(删 5% / 10% / 20% cell)。

然后报告:**哪些方法的排名在扰动下稳定,哪些排名 flaky**。这件事不需要新模型,需要一个能跑得起的 pipeline。我已经在做这件事,慢(每周增量迭代)。

### 3.2 可复现、纯 CPU 的基线

跑 BEELINE 这个量级的实验通常需要 GPU。**意味着大部分同行不能复现**。我一个 CPU-friendly 的 baseline:

- **BayesianNet**(自实现,在写)
  - 用 Var Bayes / drop-on-line priors 拼成 ensemble
  - 全部 NumPy + multiprocessing,无需 GPU
  - README 里有一个 24 小时的 budget 报告

这件事的价值不在"赢 leaderboard",在"任何人都能在笔记本上复现我"。benchmark 报告里附**"可复现性矩阵"**—— 哪些方法在 CPU budget 下能跑,这就是后来人能用的。

### 3.3 Wet-lab actionable

**最关键的判断**:一个 GRN 推断 pipeline 是不是"湿实验能用"?

具体说:

1. **输出可解释性**——能把"这个 edge 是高置信"的判定说清楚,不是黑盒。
2. **输入最小化**——不需要 50 个数据点联合,只需要 5-10 个数据点也能给出推测(对单细胞实验很难,但对 bulk RNA-seq 是合情理的)。
3. **下游假设生成**——输出一个能转成"做这个 knock-out 实验是否合理"的报告,不只是"这里有 TF → G"。

这件事没法在 BEELINE 里直接验证。它需要跟 wet-lab 实验室合作。

---

## 四、为什么我"prefer my own pipeline"而不去蹭 scGPT / GeneFormer 这类大模型

这个问题经常被问起。我的回答分两层:

**第一层:模型能力与稳健评测都还没到位**。scGPT 在 7 个数据集上刷出过一些数值,但它对扰动的稳健性、跨 cohort 的一致性、与生物学先验对齐的程度,都是有争议的。具体例子:scGPT 论文里 EPR 比 PIDC 高 ~10 个点,但是当 codebase 升级几个版本之后,这个差缩到 ~3 点(来自 community review,不在公开 leaderboard)。一个"领先 10 点"的方法 vs 一个"领先 3 点"的方法,功能上不一样。

**第二层:即便 leaderboard 真有效,我也不是这里的主线人物**。单细胞 foundation model 是 大组的事(scGPT 来自 Stanford PRP,GeneFormer 来自 Regeneron)。他们能 scale、能集资源、能发 NCS。能做有价值贡献的学生通常的路线是 **做他们的下游应用或者评测**,而**不是想跟他们拼 scale**。后者的空间已经不大。

我现在的方向更倾向于"做评测 + 做下游应用 + 做小而精的可复现 baseline",这就是为什么选择扑在一根具体的管道上。

---

## 五、AI4bio 转折点,本科起步的几个立场

这些不是"必须"对的项目标准,是我个人立场。给你参考。

### 5.1 别赌 scale,赌定义与可复现

如果一定要选,**做这个方向的定义者比做方向的追随者更值**。Leaderboard 是定义者能控制的,有 plumbing 才有 leadership。

### 5.2 选择"小而好复现"的研究对象

对比"在 BEELINE 上刷第一名"与"做 BEELINE 上的复现审计"。后者更小,但落地价值更高。当我们去做"哪几个方法是真正可复现的 leader",我们写出来的报告对所有做 downstream 的人都用。

### 5.3 关注湿实验的反馈 cycle

把你写出来的 pipeline 给至少一个湿实验实验室看 → 让他们用 → 用完反馈哪些 TRR 真的做了出来 → 用这些反馈更新 pipeline。**这是一个 ~1 个月一个 iteration 的 loop**。论文里的"ground-truth"不会主动告诉你哪里做对。

### 5.4 在工具基础设施上投入

你自己写一个 Beeline 版本的 evaluator。开始 ~500 行 Python,2 周写完。之后你所有后续 paper 都能复用。

### 5.5 与 scale 进行"反联盟"

做"小模型在更小数据上能不能做出来"的工作。这类工作在 NLP 圈里有 [Big-bench small models](https://github.com/google/BIG-bench),在 biology 里尚少。**这是一个有空间的空白**。

---

## 六、我不做的事(以及我不做的事的原因)

- **不押 单细胞 foundation model 训练** —— 资源不是我能动的。这不是"不上进",是"我不在那个位置上"。

- **不押 同一份 BEELINE 上的方法发布** —— 同质化在 rank-1 那个位置会让你短期赢得 1 篇 paper,长期输,以及你会跟 leaderboard 的不稳态绑定。

- **不押 缺乏 ground-truth 的纯 transcription-level 工作** —— 短期内模型能力增长比 ground-truth 涨得快,paper 就会变成"模型拟合一个弱标签"而不是"科学进展"。

- **不向 PubPeer-style / Twitter 论战里投入精力** —— 写 paper 比辩论战赢 +1 名引用少 5 个引用。

---

## 七、下一篇要做的事(对自己)

把上面 3 个方向(§3.1, 3.2, 3.3)分别开项目:

1. **beeline-audited**:自己的 BEELINE apples-to-apples 复现项目,目标:repo + arxiv preprint,1 个 Q1 的 reproducibility paper。
2. **bayesian-net-cpu**:NumPy + multiprocessing 的 GRN baseline,目标:提供可复现 + 跑得快的 reference implementation。
3. **wet-lab-pilot**:跟本校或附近 wet-lab 谈单细胞 + GRN 联合项目,目标是 1 次实际能运转的合作。

每个项目独立推进,每个 1-3 个月内能落一个 milestone。

如果你对我的方向有兴趣:**最想看到外部给的反馈是** §3.1 (复现审计) — 这个有最大概率出 paper,也能对 community 有最大贡献。合作 / 反馈 / 直接复现,都可以到 [sk_hwong@outlook.com](mailto:sk_hwong@outlook.com)。

---

## 引用与延伸阅读

- Pratapa, A., et al. (2020). "Benchmarking algorithms for gene regulatory network inference from single-cell transcriptomic data." *Nature Methods*, [DOI:10.1038/s41592-019-0690-6](https://doi.org/10.1038/s41592-019-0690-6).
- Aibar, S., et al. (2017). "SCENIC: single-cell regulatory network inference and clustering." *Nature Methods*.
- Huynh-Thu, V.A., et al. (2010). "Inferring regulatory networks from expression data using tree-based methods." *PLoS ONE* (GENIE3).
- Moerman, T., et al. (2019). "GRNBoost2 and Arboreto: efficient pre-processing for gene regulatory network inference." *Bioinformatics*.
- Cui, H., et al. (2024). "scGPT: toward building a foundation model for single-cell multi-omics using generative AI." *Nature Methods*, [DOI:10.1038/s41592-024-02201-0](https://doi.org/10.1038/s41592-024-02201-0).
- Theodoris, C.V., et al. (2023). "Transfer learning enables predictions in network biology." *Nature*, [GeneFormer](https://www.nature.com/articles/s41586-023-06456-9).
- Yang, F., et al. (2022). "scBERT as a large-scale pretrained deep language model for cell type annotation of single-cell RNA-seq data." *Nature Machine Intelligence*.
- Lotfollahi, M., et al. (2022). "scvi-tools: a library for deep probabilistic analysis of single-cell omics data." *Nature Biotechnology*.
- Megill, J.S., et al. (2021). "Cell Typist." *Science* — reference for cell annotation benchmarking methods.
- Boiarsky, R., et al. (2023). "CellRank 2 / dynamical systems for cell-fate prediction." *Nature Methods*.

一些我推荐的基本立场 / 工作流笔记:

- **How to Find Research Ideas**(钱志云):https://www.cs.ucr.edu/~yongzheng/papers/How_to_find_research_ideas.html
- **Three-pass** method(Keshav):http://ccr.sigcomm.org/online/files/p83-keshavA.pdf
- **cs231n 学习笔记**(本博客):CNN / Transformer / 视觉评测
- **HANDS ON LLM**(本博客):LLM pretraining / SFT / DPO 操作面

---

最后一条:**这篇不是说服**。这是把决策公开,让同方向的人在协作之前知道我站在哪里 —— 我赌 wet-lab-actionable 上的一个具体口径,不赌 leaderboard 第一。**这是本科起步阶段的合理半径**,我相信这个立场在 ≥2 年里会自然演化(可能调整,可能不动)。

如果觉得这篇文章可以引发思考,而不是赞同,我目的达到。
