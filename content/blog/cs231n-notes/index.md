---
title: 'CS231n 学习笔记'
summary: 'Stanford CS231n (CN-DETR-style) study notes — convolutional networks, vision, and deep learning foundations.'
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

CS231n 学习笔记。

开个新坑监督一下自己，形成一份系统学习笔记。

三个大作业和课程目标是在 15–20 天内完成，再抽空复习动手学深度模型（如有时间会整理为笔记）。

趁学期初发力，假期深感自己的懈怠。早期进度会稍快一些；后期随难度增加适当放缓。课程笔记不会太长，但课程作业我会写得详细一些。

## DAY1（25.9.2）

### C1. 卷积神经网络简介

CV 是计算机视觉宇宙的中心（笑）。

1. 对于难以处理的图像，我们可以做适当的分割——我们不知道像素组合起来是人，但可以提取所有疑似人的像素（用**图论解决图像分割**问题）。
2. **SIFT**（尺度不变特征转换）通过匹配关键点而非匹配整体来进行检测，具有很好的鲁棒性。
3. 图像特征的维度一般很高，因此算法很容易**过拟合**——按我现在的理解，提前停止训练或增加数据量可以缓解。
4. **ImageNet** 是一个很大的目标识别数据集，相关比赛往往使用 top5 标准来衡量。

第一课的知识密度不高，主要在介绍 CV 和 CS231n 课程安排，但讲得有趣且娓娓道来。

### C2. 图像分类

1. 采用**数据驱动算法**：不针对每个类别写规则，而是**对每一类物体找大量样例灌给计算机学习，归纳模式规律、训练分类器**，再用训练好的模型识别新图像。

2. 最近邻算法（NN）

$$
d_{1}(I_{1}, I_{2}) = \sum_{p} |I^{p}_{1} - I^{p}_{2}|
$$

其中 $p$ 为像素点，$I^{p}$ 表示第 $p$ 个像素点的值。两张图片的 $L_1$ 距离即逐像素求差值的绝对值之和；一模一样时距离为 0。

```python
import numpy as np
class NearestNeighbor(object):
    def __init__(self):
        pass
    def train(self, X, y):
        """X: N x D, 每行是一个样本; y: 长度为 N 的标签数组"""
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

如果用 $L_2$ 距离：

```python
distances = np.sqrt(np.sum(np.square(self.Xtr - X[i, :]), axis=1))
```

$L_1$ 距离依赖于坐标轴，$L_2$ 距离形成一个圆，不依赖坐标轴。面对差异时 $L_2$ 比 $L_1$ 更不能容忍大差异——**相对 1 个巨大差异，$L_2$ 更倾向于接受多个中等差异**。

3. K 最近邻（KNN）

KNN 思想：找最相似的 $k$ 个图片的标签，$k$ 个标签中数量最多的标签作为对测试图片的预测。

超参数需要预先设置，借助于实验寻找最优取值。

```python
# 取前 1000 训练样本作为验证集
Xval_rows = Xtr_rows[:1000, :]
Yval      = Ytr[:1000]
Xtr_rows  = Xtr_rows[1000:, :]
Ytr       = Ytr[1000:]

validation_accuracies = []
for k in [1, 3, 5, 10, 20, 50, 100]:
    nn = NearestNeighbor()
    nn.train(Xtr_rows, Ytr)
    Yval_predict = nn.predict(Xval_rows, k=k)
    acc = np.mean(Yval_predict == Yval)
    validation_accuracies.append((k, acc))
```

交叉验证：将数据集分组后循环利用，避免单次划分带来的偏差。

4. KNN 优缺点

- 优点：易于理解、实现简单；训练仅保存数据，不需要耗时。
- 缺点：测试开销大，每个测试样本都要和所有训练样本比较；实际应用更关注测试效率。

5. 参数模型

线性分类器由两部分组成：

**① 评分函数（score function）**——原始图像到类别分值的映射。
**② 损失函数（loss function）**——量化分数与真实标签的不一致。

$$
f(x_i, W, b) = W x_i + b
$$

其中 $W$ 为权重矩阵，$b$ 为偏置项。

## DAY2（25.9.3）

### C3. 损失函数与优化

1. **损失函数**（Loss / Cost / Objective）$L$ 衡量对预估结果的不满意程度：

$$
L = \frac{1}{N} \sum_{i=1}^{N} L_i(f(x_i, W), y_i)
$$

2. 多类 SVM 损失

$$
L_i = \sum_{j \ne y_i} \max(0, s_j - s_{y_i} + \Delta)
$$

```python
def L_i(x, y, W):
    delta = 1.0
    scores = W.dot(x)
    correct_class_score = scores[y]
    D = W.shape[0]
    loss_i = 0.0
    for j in range(D):
        if j == y:
            continue
        loss_i += max(0, scores[j] - correct_class_score + delta)
    return loss_i

def L_i_vectorized(x, y, W):
    delta = 1.0
    scores = W.dot(x)
    margins = np.maximum(0, scores - scores[y] + delta)
    margins[y] = 0
    return np.sum(margins)
```

3. 完整的 SVM 损失：**数据损失 + 正则化损失**

$$
L = \frac{1}{N} \sum_i L_i + \lambda R(W)
$$

4. 数值梯度法

$$
\frac{df(x)}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}
$$

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

## DAY3（25.9.4）

### ASSIGNMENT 1
