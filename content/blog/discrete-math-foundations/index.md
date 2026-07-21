---
title: '离散数学（核心基础）'
summary: '离散数学核心基础复习笔记 —— 命题逻辑公式化简、范式理论、集合论、关系、图论基础,每节配典型例题和真题思路,兼顾期末复习与期末后的"什么时候回看这一题"。'
date: '2025-10-01'
authors:
  - sky-huang
tags:
  - Course Notes
  - Mathematics
  - Foundations
categories:
  - course-notes
---

> 适用:期末复习 / 考研基础阶段 / 自学者建立核心概念模型。例题从经典题里挑,把"解题套路"和"考试经常挖的坑"标出来。

---

## 一、命题逻辑

### 1.1 命题符号化

把自然语言命题翻译成逻辑符号,是后续公式化简的前提。

**联结词优先级**:
$$
\neg > \wedge > \vee > \to > \leftrightarrow
$$

外加:**括号**永远优先。

**例子**:命题 "虽然今天是工作日,但如果不下雨,我就去跑步"。

把"今天不下雨"记为 $W$,"我去跑步"记为 $R$,"今天工作日"记为 $W$。"虽然 ... 但 ..." 翻译为合取。"如果 ... 就 ..." 翻译为 $\to$。

$$
W \wedge (W \to R)   \; — \; 注意 $W$ 重名用上下文区分
$$

练习:`"除非明天不下雨,否则我们去散步"` 翻译为 $(\neg \neg W) \to G$ 还是 $\neg W \vee G$?这是一道经典的"除非"语义题,标准答案是 $W \to G$ 的对偶。

### 1.2 公式分类与化简

三种公式:

- **永真式(重言式)**:真值表每个解释下都真
- **永假式(矛盾式)**:真值表每个解释下都假
- **可满足式**:至少一个解释下真

**核心化简工具**:

$$
\begin{aligned}
\text{德摩根律:} \quad & \neg(P \wedge Q) \equiv \neg P \vee \neg Q \quad ; \quad \neg(P \vee Q) \equiv \neg P \wedge \neg Q \\
\text{双否:} \quad & \neg\neg P \equiv P \\
\text{蕴含等值:} \quad & P \to Q \equiv \neg P \vee Q \quad ; \quad P \leftrightarrow Q \equiv (P \wedge Q) \vee (\neg P \wedge \neg Q) \\
\text{吸收律:} \quad & P \vee (P \wedge Q) \equiv P \\
\text{假言易位:} \quad & P \to Q \equiv \neg Q \to \neg P
\end{aligned}
$$

**典型题**:

> 把 `((¬P∨Q)↔(Q∨¬P))∧P` 化简。

注意到:`¬P ∨ Q ≡ Q ∨ ¬P`(换序律在 $\vee$ 下成立)又 `¬P ∨ Q ≡ P → Q`。所以 `¬P ∨ Q` 和 `Q ∨ ¬P` 实质相同,**等值式两边真值一致**。

剩下的 `(P) ∧ P` (因为 `(P) ∧ anything-equivalent-to-P` = `P ∧ P` = $P$)实际上化简:`(真) ∧ P` = $P$。

答案:**$P$**。

### 1.3 范式理论(考试重点)

#### 主析取范式(PDNF)

$$
P \equiv \bigvee_{(P \text{ 在解释 } e \text{ 下真})} m_e
$$

每个 $m_e$ 都是"把解释 $e$ 编码成合取",即把解释 $e$ 下为真的命题变元为 $x$、为假的写 $\neg x$,合起来。

**做法**:
1. 列真值表
2. **找出 $P$ 在哪些解释下为真**
3. 每个 $P$ 为真的解释 $\to$ 一个极小项
4. 极小项之间用 $\vee$ 串起来

#### 主合取范式(PCNF)

同理,找 $P$ 为假的解释,每个写成一个极大项 $M_i$,然后 $\bigwedge M_i$。

### 1.4 演绎证明

**推理规则**:

- **MP**:$P \to Q,\; P \;\Rightarrow\; Q$
- **MT**:$P \to Q,\; \neg Q \;\Rightarrow\; \neg P$
- **HS**:$P \to Q,\; Q \to R \;\Rightarrow\; P \to R$
- **DS**:$P \vee Q,\; \neg P \;\Rightarrow\; Q$

**经典真题**:

> 前 1:若 6 是偶数,则 2 不整除 7。
> 前 2:5 非素或 2 整除 7。
> 前 3:5 是素数。
> 结论:6 是奇数。

设 $E$:6 是偶, $D$:2 整除 7, $P$:5 是素。

- 前 1: $E \to \neg D$
- 前 2: $\neg P \vee D$
- 前 3: $P$

推导:

由 HS 简化版的 P2 + P3:得 $D$ (DS:$\neg P \vee D$, $P$ $\Rightarrow$ $D$)

由 P1 ($E \to \neg D$) MT:得 $\neg E$

$\neg E$ 即"6 不是偶数" = "6 是奇数"。

**结论成立**。

---

## 二、集合论(简)

集合是离散数学的底座。要点:

- $A \subseteq B$:全属于
- $A \subsetneq B$:真属于
- $A = B$:互为子集
- 幂集 $\mathcal{P}(A)$:包含所有子集的集合,$|\mathcal{P}(A)| = 2^{|A|}$
- 集合运算:$\cup, \cap, \setminus, \complement, \triangle$ (对称差)
- 分配律 / 德摩根律 / 幂等律 / 双补律

**关键**:用一阶逻辑化的语言理解集合($\in, \subseteq, \forall, \exists$)。这一点直接连到"谓词逻辑"。

---

## 三、谓词逻辑(简)

引入量词 $\forall$ 和 $\exists$。

**核心等价**:

$$
\begin{aligned}
\neg \forall x\, P(x) &\equiv \exists x\, \neg P(x) \\
\neg \exists x\, P(x) &\equiv \forall x\, \neg P(x)
\end{aligned}
$$

**小心**:量词顺序很重要。`$\forall x \exists y, x + y = 0$`(对每个 x 都能找到反例)与 `$\exists y \forall x, x + y = 0$`(有一个 y 对所有 x 都合)完全不同。

**重要性质**:

$\exists$ 右结合(不强求左结合),$\forall$ 左结合。这与命题逻辑的 $\wedge, \vee$ 一致。

---

## 四、关系

### 4.1 基本概念

$R$ 是 $A \times B$ 的子集。如果 $A = B$,就说是 $A$ 上的关系。

**矩阵表示**:$m_{ij} = 1$ 当 $a_i R a_j$。

**图表示**:有向图的边集。

### 4.2 关系的性质

| 性质 | 矩阵特征 | 图特征 |
|---|---|---|
| 自反 $\forall a: aRa$ | 单位矩阵 $I$ 元素全是 1 | 每个顶点有自环 |
| 反自反 $\forall a: \neg aRa$ | 对角全是 0 | 没有自环 |
| 对称 $\forall a, b: aRb \to bRa$ | 矩阵对称 | 边两两对称 |
| 反对称 $\forall a, b: aRb \wedge bRa \to a = b$ | 对称位置不能同为 1 | 无双向边 |

### 4.3 等价关系

自反 + 对称 + 传递 = **等价关系**。可以诱导划分:商集 $A / R$ 是所有等价类的集合。

例:整数模 4 同余是等价关系,4 个等价类是 $\{0,4,8,...\},\{1,5,9,...\},\{2,6,10,...\},\{3,7,11,...\}$。

### 4.4 偏序关系

自反 + 反对称 + 传递 = **偏序关系**。用于定义 hasse 图(去掉传递、自反可访问的边)。

---

## 五、图论基础

### 5.1 基本对象

- 有向图 / 无向图
- 顶点数 $|V|$, 边数 $|E|$
- **握手定理**:$\sum_{v \in V} \deg(v) = 2|E|$(每条边贡献 2)
- **完全图** $K_n$:每个顶点都连边, $|E| = n(n-1)/2$
- **二部图**:可以 2-着色,没有奇数环

### 5.2 路径与连通

- **简单路径**:不重复顶点
- **连通性**:无向图中每对顶点都有路径
- **欧拉回路**:经过每条边恰好一次的回路;充要是连通 + 每顶点偶数度
- **哈密顿回路**:经过每个顶点恰好一次的回路;无简单充要条件(完全图必有)

### 5.3 树

$n$ 个顶点的树 = 连通 + 无环 = 连通 + $|E| = n - 1$ = 无环 + $|E| = n - 1$。

树的性质:
- 任意两顶点间有唯一简单路径
- 加任意一条边形成恰好一个环
- 删去任意非叶边分裂成两棵树

**重要的数据结构 / 算法视角**:
- 二叉树、BST(搜索树)、红黑树(平衡)
- B/B+树(数据库索引)
- Trie(前缀树)
- Huffman 树(信息论编码)

### 5.4 算法相关

- **Dijkstra**(单源最短路径,前提:边权非负),$O((V + E) \log V)$
- **Bellman-Ford**:任意边权,但 $O(VE)$
- **Floyd-Warshall**:全对最短, $O(V^3)$
- **Kruskal**(最小生成树):用并查集, $O(E \log V)$
- **Prim**: $O((V + E) \log V)$
- **拓扑排序**:DFS + 入度法, $O(V + E)$

---

## 六、代数系统(可选)

- 半群 / 幺半群 / 群 / 环 / 域
- 同态 / 同构
- 子群 / 生成元 / 陪集 / Lagrange 定理

如果时间紧,本科 level 一般不深挖群论。但 **有限域 $\mathbb{F}_p$ 在密码学里最常用**,知道存在即可。

---

## 七、与 AI 的连接(为什么离散数学重要)

| 离散数学概念 | 在 AI 里 |
|---|---|
| 集合论 | 数据集 / 索引结构 |
| 关系 / 等价类 | 聚类 / 模态转换 |
| 图论 | GNN / Knowledge Graph / 程序依赖图 |
| 树 | 决策树 / 语法树 / Huffman |
| 谓词逻辑 | 一阶逻辑推理 / ILP |
| 范式 | 自动定理证明的核心架构(SMT) |
| $\mathbb{F}_p$ | 加密 / 隐私计算 / ZKML |

具体到我的方向:**单细胞数据可以建模成图**,然后用图论工具做 subnetwork / 路径挖掘。BEELINE 这类 GRN benchmark 的真子集识别用的就是图算法。

---

## 推荐练习资源

- 屈婉玲、耿素云《离散数学》(教材主流)
- Kenneth Rosen《Discrete Mathematics and Its Applications》(英文最推荐)
- LeetCode 上 "Lock-in" 系列图论题 (BFS / DFS / Dijkstra)
- 课后真题 + 往年卷

最后一条原则:**离散数学不是计算题库,是抽象方法**。把概念掌握到你能在你做的领域里重新讲出来,考试反而简单。

---

下一篇 **[AI4bio 转折点](/blog/ai4bio-turning-point/)** 里的图算法例子,与本节"图论基础"互为补充。
