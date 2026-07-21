---
title: 'CS231n 学习笔记'
summary: 'Stanford CS231n (李飞飞组) 卷积神经网络视觉识别课程完整学习笔记 — KNN / SVM / Softmax / 全连接神经网络 / 反向传播 / CNN / ResNet / 迁移学习 / 检测分割 / 可视化,加 6 个月后回看与 AI4Science 的连接。'
date: '2025-09-02'
authors:
  - sky-huang
tags:
  - Course Notes
  - Computer Vision
  - Deep Learning
  - CS231n
categories:
  - course-notes
---

CS231n 学习笔记(完整版)。

一份系统学习笔记。三个大作业和课程目标在 15-20 天内完成,加上动手学深度模型(如有时间整理为笔记)。

趁学期初发力,假期深感自己的懈怠。早期进度快一些,后期随难度增加适当放缓;课程笔记不会太长,但课程作业我会写得详细一些。

---

## DAY1 (25.9.2) — 课程导论 + KNN

### C1. 卷积神经网络简介

CV 是计算机视觉宇宙的中心(课上笑谈)。

1. 对于难以处理的图像,我们可以做适当的分割 —— 我们不知道像素组合起来是人,但可以提取所有疑似人的像素(用**图论解决图像分割**问题)。
2. **SIFT**(尺度不变特征转换)通过匹配关键点而非匹配整体来进行检测,具有很好的鲁棒性。
3. 图像特征的维度一般很高,因此算法容易**过拟合** —— 提前停止训练或增加数据量可缓解。
4. **ImageNet** 是一个很大的目标识别数据集,相关比赛往往使用 top-5 标准来衡量。

第一课知识密度不高,主要在介绍 CV 和 CS231n 的整体框架 —— 但讲得有趣。

### C2. 图像分类 — 数据驱动 + KNN

**核心范式转换**:不针对每个类别写规则,而是对每一类物体找大量样例灌给计算机学习,归纳模式规律、训练分类器,再用训练好的模型识别新图像。

#### 最近邻算法 (NN)

$$
d_{1}(I_{1}, I_{2}) = \sum_{p} |I^{p}_{1} - I^{p}_{2}|
$$

其中 $p$ 为像素点,$I^{p}$ 表示第 $p$ 个像素。两张图片的 $L_1$ 距离即逐像素差值绝对值之和。

```python
import numpy as np

class NearestNeighbor:
    def __init__(self):
        pass
    def train(self, X, y):
        # 只把数据记住,这是训练
        self.Xtr = X
        self.ytr = y
    def predict(self, X):
        num_test = X.shape[0]
        Ypred = np.zeros(num_test, dtype=self.ytr.dtype)
        for i in range(num_test):
            distances = np.sum(np.abs(self.Xtr - X[i, :]), axis=1)
            min_index = np.argmin(distances)
            Ypred[i] = self.ytr[min_index]
        return Ypred
```

如果用 $L_2$ 距离:

```python
distances = np.sqrt(np.sum(np.square(self.Xtr - X[i, :]), axis=1))
```

> $L_1$ 距离形成的判别边界贴近坐标轴;$L_2$ 距离形成一个圆。$L_2$ **相对 1 个巨大差异,更倾向于接受多个中等差异**(因为差值平方)。

#### K 最近邻 (KNN)

KNN 思想:找最相似的 $k$ 个图片的标签,数量最多的标签作为预测。

```python
# 验证集划分
Xval_rows = Xtr_rows[:1000, :]
Yval       = Ytr[:1000]
Xtr_rows   = Xtr_rows[1000:, :]
Ytr        = Ytr[1000:]

validation_accuracies = []
for k in [1, 3, 5, 10, 20, 50, 100]:
    nn = NearestNeighbor()
    nn.train(Xtr_rows, Ytr)
    Yval_predict = nn.predict(Xval_rows, k=k)
    acc = np.mean(Yval_predict == Yval)
    validation_accuracies.append((k, acc))
```

#### KNN 优缺点

- **优点**:易于理解,实现简单,训练不耗时(只是存数据)
- **缺点**:测试开销巨大 —— 每个测试样本都要与所有训练样本比较。实际应用更关注测试效率

#### 引入参数模型

$$
f(x_i, W, b) = W x_i + b
$$

其中 $W \in \mathbb{R}^{K \times D}$ 为权重矩阵,$b \in \mathbb{R}^{K}$ 为偏置项。这是参数模型的雏形 —— 训练找 $W$,预测只需与 $W$ 做一次乘加。

---

## DAY2 (25.9.3) — 损失函数与优化

### C3. 多类 SVM 损失 (Multiclass SVM Loss)

**Loss 量化"评分与真实标签"的不一致**。目标:找一个 $W$ 让 $L$ 最小。

$$
L = \frac{1}{N} \sum_i L_i(f(x_i, W), y_i)
$$

其中:

$$
L_i = \sum_{j \ne y_i} \max(0, s_j - s_{y_i} + \Delta)
$$

例:某张猫的图得分向量 $(3.2, 5.1, -1.7)$,真实类 cat = 0(5.1 行),则:

$$
L = \max(0, 5.1 - 3.2 + 1) + \max(0, -1.7 - 3.2 + 1) = 2.9 + 0 = 2.9
$$

向量化实现:

```python
def L_i_vectorized(x, y, W):
    delta = 1.0
    scores = W.dot(x)
    margins = np.maximum(0, scores - scores[y] + delta)
    margins[y] = 0
    return np.sum(margins)
```

完整 SVM 损失 = 数据损失 + 正则化损失:

$$
L = \frac{1}{N} \sum_i L_i + \lambda R(W)
$$

正则化项 $R(W)$ 通常取 $L_2$ 范数,作用:防止训练数据上过拟合,鼓励小的权重。

### C4. Softmax(交叉熵)损失

$$
L_i = -\log\left(\frac{e^{s_{y_i}}}{\sum_j e^{s_j}}\right)
$$

数值稳定性做法:每个 $s$ 减最大值 $C$。

### C5. 优化方法

$$
W \leftarrow W - \alpha \nabla_W L
$$

简单 SGD → 小批量 + 动量 → Adam(动量 + 自适应学习率)。当代默认 AdamW(weight decay 与 Adam 解耦)。

### C6. 反向传播

**核心**:链式法则。计算图正向传播把中间值缓存,反向传播用这些缓存值算梯度。

```python
def eval_numerical_gradient(f, x):
    fx = f(x)
    grad = np.zeros(x.shape)
    h = 0.00001
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        ix = it.multi_index
        old_value = x[ix]
        x[ix] = old_value + h
        fxh = f(x)
        x[ix] = old_value
        grad[ix] = (fxh - fx) / h
        it.iternext()
    return grad
```

---

## DAY3 (25.9.4) — 神经网络入门

### C7. 全连接神经网络

单隐层就是一个超参线性模型叠一个非线性激活:

$$
f(x) = W_2 \sigma(W_1 x + b_1) + b_2
$$

常用激活:ReLU(max(0,x))、Sigmoid、Tanh。当代隐藏层几乎都用 ReLU/GELU/SwiGLU。

### C8. 反向传播回到神经网络

每一层是 $y = W x$ 和 $\sigma$ 的组合,梯度通过链式法则反传。框架(autograd)在 2014 年前后解决这件事,PyTorch / JAX 让反向传播变成一行 `.backward()`。

---

## DAY4-7 — CNN 主体

### C9. 卷积与池化

卷积层输出尺寸:
$$
(N + 2P - F) / S + 1
$$

其中 $N$ 输入尺寸,$P$ padding,$F$ filter size,$S$ stride。

**关键直觉**:
- 同一 filter 扫整张图 → 参数共享 → 平移不变性
- 多层叠加自然学到层级特征(edge → texture → part → object)

### C10. 经典架构:LeNet / AlexNet / VGG / GoogLeNet / ResNet

**ResNet 是分水岭**。引入残差连接:
$$
y = F(x, \{W_i\}) + x
$$

让"什么都不学"(identity)成为可能 —— 堆深网络不再退化。

代码层面,ResNet 的实现关键就是 `out += identity`,短接一条 1×1 conv 处理 channel 变化。

### C11. 训练技巧

- 数据增强(随机裁剪、翻转、ColorJitter)
- 权重初始化(Xavier / He)
- BatchNorm / LayerNorm
- 学习率 warmup + cosine decay
- 早停 / 模型平均 / EMA

---

## DAY8-10 — 视觉感知任务

### C12. 检测与分割

- **Detection**:R-CNN → Fast/Faster R-CNN → SSD → RetinaNet → YOLO
- **Segmentation**:FCN → U-Net → DeepLab(Mask R-CNN 一并搞定)

U-Net 的 encoder-decoder + skip connection 几乎是所有密集预测的底模。

### C13. 注意力与 Transformer

ViT 把图像分成 16×16 patch,每块当成一个 token,然后就是标准的 Transformer encoder。多尺度金字塔(Swin / PVT)让 Transformer 在视觉上真正实用。

---

## 作业要点(我能记住的)

### Assignment 1 — KNN / SVM / Softmax

需要手写:
- L2 距离的向量化(避免双重循环)
- SVM loss 含正则化的向量化
- Softmax 含数值稳定的 log-sum-exp
- 数值梯度做 sanity check

要点:**别抄 nn.torch 的 API**,这作业就是为了让你重新写一遍前向/反向。

### Assignment 2 — 全连接神经网络

需要手写:
- 各种层的反向(SVM/softmax/全连接/ReLU)
- SGD + momentum + dropout
- 训练一个小网络在 CIFAR-10 上

要点:**用 units test 验证你每一层梯度都对**(跟 numerical_gradient 比较)。

### Assignment 3 — CNN

需要实现:
- 卷积层(朴素 im2col 或直接循环)
- 池化层
- BatchNorm
- 整个 CNN 在 CIFAR-10 上 train 到 ~75% 以上

要点:**Conv 是这次作业最坑的部分** —— 朴素实现 $O(C \cdot C' \cdot K^2 \cdot N \cdot H \cdot W)$,需要向量化。

---

## 6 个月后回看

课结束后 6 个月再看,有几条经验突然变清晰:

1. **CS231n 教的不是"怎么分类"而是"现代深度学习的脚手架"**。Transformer / 注意力 / 多尺度金字塔 / 数据增强 / 训练 trick —— 这些是真正的可迁移资产。
2. **从 CNN 到 ViT 是一个 reduction**。把图像当成序列(patch sequence)就把视觉任务完全统一到 NLP 的工具链下。这个 unification **直接让 single-cell foundation model 成为可能**(把每个基因当成 token,模型就是 transformer)。
3. **训练 pipeline 比架构重要**。CS231n A3 上过 75% 难吗?模型架构不复杂,但 learning rate / warmup / augmentation / EMA 设对了才到得了。这是为什么我后来去读 trl / vLLM / Ray 的 training pipeline 源码。
4. **CV 的 evaluation 与 bio 的 evaluation 现在面对同一个问题**:leaderboard 是否可信。这一篇**[AI4bio 转折点](/blog/ai4bio-turning-point/)** 就是从这里长出来的。

---

## 与 AI4Science 的连接

具体到我的方向(scRNA-seq GRN inference),从 CS231n 学到的东西继续发光:

- 一个 [Vision Transformer 的 attention map 思路](https://arxiv.org/abs/2010.11929)几乎可以一对一搬到 **gene-gene attention** 上(scGPT、scBERT 都做这件事)
- U-Net 的 skip connection 在 **[GeneFormer](https://huggingface.co/ctheodoris/GeneFormer)** 的 decoder 里都有类似的生物学解释
- 数据增强策略(random gene masking,Mix-up 在 expression matrix 上)在 CS231n 训练 pipeline 和 scRNA-seq pretraining 之间迁移

下一篇 **[AI4bio 转折点](/blog/ai4bio-turning-point/)** 是从这一篇里伸出来的"leaderboard 与湿实验可用的 pipeline 路线之争"。两个笔记互为上下文。
