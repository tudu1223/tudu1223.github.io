---
title: '科研常用网址 / 资源 / 工具'
summary: '一份按"我用过什么、怎么用、为什么选"组织的科研资源清单 —— 找 idea / 读论文 / 写论文 / 文献管理 / 找会议 / 绘图 / LaTeX 一站式。带个人推荐顺序和入门路径。'
date: '2025-12-01'
authors:
  - sky-huang
tags:
  - Tools
  - Academic Writing
  - Resources
categories:
  - tools
---

> 这不是一份冷冰冰的工具罗列,是**我用过的、留下来的、还会再打开的**东西。
> 加了"第一次用该从哪开始"和"我为什么用这个不换成别的"。换一波之后还会有变化。

## 0. 我自己用的频次(2025-2026 春季)

| 类别 | 主力工具 | 第二选择 |
|---|---|---|
| 找 idea | arxiv-sanity / scholar inbox | Connected Papers |
| 读论文 | Zotero + Hypothes.is | PDF + 平板 |
| 写论文 | Overleaf / 本地 LaTeX | VS Code + Latex Workshop |
| 文献管理 | Zotero + Better BibTeX + DBLP | 无 |
| 找会议 | 导师 / CCF DDL | WikiCFP |
| 看数据 | Scanpy / scvi-tools | R+Seurat(实验组) |
| 训练模型 | PyTorch + Lightning | HuggingFace transformers |
| 跑下游评测 | 自写 / Awesome Lists | Papers With Code |
| 部署服务 | vLLM | TGI |

## 1. 找 idea(起步阶段最常用)

- **钱志云:How to Find Research Ideas**
  - 加州大学河滨分校教授写的找 idea 模板文章。
  - **入门必看**,尤其是本科起步阶段。
  - https://www.cs.ucr.edu/~yongzheng/papers/How_to_find_research_ideas.html
  - **我为什么用它**:写得很实战,比"读 50 篇 paper"管用。
- **Connected Papers**
  - 给定一篇 paper,可视化它在引文图里的邻居。
  - **用法**:新方向入门第一周先做一次,大概知道这个领域的拓扑。
  - https://www.connectedpapers.com/
- **arXiv-sanity**
  - Twitter 关心的 paper,smrtrl 维护,偏 ML 主线。
  - **用法**:每天通勤刷 5 分钟;按 frontier / lab 订阅。
  - http://www.arxiv-sanity.com/
- **arXiv**
  - 一手源头。每天新出的 paper,看你方向的 daily mailing。
  - https://arxiv.org/

## 2. 读论文

**两条铁律**:

1. **第一遍不细读**。先 abstract + 图 + conclusion,问自己:**这个问题我能不能用 1 句话讲给外行听**。
2. **不要从头读到尾**。找"贡献 + 实验"两节,先验它做了啥、新在哪、跟相关工作比几斤几两。

### 2.1 Three-pass 方法(Keshav 教授)

滑铁卢大学 **Srinivasan Keshav** 教授写的读论文三遍法:

1. **第一遍(5-10 分钟)**:快速鸟瞰。标题 / abstract / intro / conclusion / 标题下的副标题 / 第一次扫图 + 最后一个图。
2. **第二遍(1 小时)**:读主体,跳过证明。读完能在脑子里重建论文结构。
3. **第三遍(4-5 小时,熟练后更快)**:**逐行**推演,假设你自己是作者会怎么想 / 怎么答 reviewer。

> 链接:http://ccr.sigcomm.org/online/files/p83-keshavA.pdf

### 2.2 高效笔记法

- **Zotero + Hypothes.is**:PDF 上直接批注,自动同步到云。
- **Obsidian / Logseq**:把笔记写在本地 markdown,跨时间链,做"二次笔记"(二级页面)。
- **Notion / Obsidian**:两者各有特点。看你是喜欢双向链接(Obsidian)还是数据库(Notion)。

## 3. 写论文

### 3.1 写作工具

- **Overleaf**(在线 LaTeX 编辑器):协作、免装、模板多。
  - **建议**:有导师的话直接用,投稿时很多期刊自带模板。
  - https://www.overleaf.com/
- **VS Code + LaTeX Workshop**(本地):大项目 / 离线 / 跟 git 协作。
- **TexShop / Texpad(Mac)**:入门级,够用,但没补全。

### 3.2 写作本身

- **The Writer's Diet**(Helen Sword 教授):自动查句子臃肿的工具,挑哪些句子里有冗词。
  - https://writersdiet.com/
- **Grammarly**:语法基础款。**升级 800/年版有"语气"、"流畅度"**,更值得。
- **Phrasebank**(Manchester 大学):论文写作常用句式库。
  - https://www.phrasebank.manchester.ac.uk/
- **Writefull**(overleaf 集成):in-context 写作助手,比 Grammarly 更针对学术英语。

### 3.3 写好英语科技论文的诀窍(周耀旗)

印第安纳大学 **周耀旗** 教授的论文写作技巧分享。

- https://www.youtube.com/@zhanyaochi (YouTube)
- 重点章节可看讲座:Title / Abstract / Introduction / Results

> 关键点:**abstract 不是 intro 的缩短版**,是"问题 + 方法 + 一句话 + 结果"四段。**不要为了谦虚用 "promising" / "interesting" 来取代具体数字**。

## 4. 文献管理

### 4.1 Zotero(我主力用)

- **Zotero**:开源,免费。一键从浏览器收藏。
  - **必装插件**:
    - **Better BibTeX**:给文献稳定 citekey,论文里 `\cite{}` 用
    - **ZotFile**(老用户):PDF 改名为「作者+年份+标题」
    - **Mdnotes for Zotero**:导出 markdown 笔记
  - **数据库位置**:用 `Zotero.Storage` 自定义到 OneDrive / iCloud,多设备同步。
- **Zotero 高级版**如果需要更多存储:65 GB $30/年,但通常免费够。

### 4.2 DBLP 一键导入

- **DBLP**(德国):https://dblp.org/, CS 论文作者表,一键 `.bib` 导出。

> 关键:`dblp key = author:year:title_token`,能用这个就能复制 BibTeX。

### 4.3 文献数据库构建

清华大学网安博士生写的教程:**用 Zotero + DBLP 建立自己的论文数据库**(一步到位的 .pdf 自动重命名 + BibTeX 自动导出 + 跨学科分类)。

- https://github.com/Rqixuan/Zotero-based-research-database

## 5. 找会议 / 评审 / 投稿

- **CCF DDL**:https://ccfddl.com/,CCF 推荐会议截稿日期聚合,**中文**,极好用。
- **WikiCFP**:http://www.wikicfp.com/cfp/,全会议列表(信号 / 系统都有),但 UI 较旧。
- **Conference Partner(会伴)**:https://www.conferencepartner.com/,收 rate / topic / deadline / ccf 类别。
- **CORE Conference Portal**:https://core.edu.au/conference-portal,会议排名 A*/A/B/C。
- **Conference Rank**(ERA / Qualis):https://www.conferenceranks.com/,综合排名查询。
- **Google h5 index**:https://scholar.google.com/citations?view_op=metrics_intro,查会议的 H5(侧面反映录用难)。
- **AI Stats**(Stats 顶会):https://www.aistats.org/,NeurIPS/ICML/AISTATS/IJCAI/ICLR/UAI 主线。

**我的投稿选会顺序**:

1. 先看过几个 leaderboard(看相关工作引用谁最多)
2. 去 CCF DDL 看 timeline
3. 在 Google Scholar 看会议近三年 h5
4. 加进 zotero 的 conference timeline 标签

## 6. 数据 / 评测 / 复现

- **Papers With Code**:https://paperswithcode.com/,paper + code + benchmark 三件套。
- **HuggingFace**:hub + datasets + 评测样例。
- **Awesome 系列**(GitHub):每个方向都有 awesome-xxx 仓库(sc-foundation-model / awesome-bioinfomatics / 等等)。
- **scRNA-seq 评测**:
  - [BEELINE](https://github.com/Marzyo/BEELINE):GRN 推断 benchmark 标杆
  - [scIB](https://github.com/theislab/scIB):批次整合 benchmark
  - [OpenProblems](https://openproblems.bio/):single-cell 各种任务的 leaderboard

## 7. LaTeX 资源

- **Tables Generator**:https://www.tablesgenerator.com/,所见即所得写 latex 表格。
- **LaTeX Tables**:https://www.latex-tables.com/,同上,UI 好一点。
- **Mathpix Snip**:截屏直接 OCR 成 LaTeX 公式。论文里的数学方程式必备。
- **Overleaf 模板库**:https://www.overleaf.com/latex/templates,期刊 / 会议 / 大学 / 简历全覆盖。
- **Detexify**:https://detexify.kirelabs.org/classify.html,手写符号找 LaTeX 命令。

## 8. 插图 / 排版 / 出片

- **Inkscape**(开源矢量):光栅 / 矢量混合制作,适合 figure 后期拼装。
- **TikZ**:LaTeX 内的矢量绘图,figure 全 LaTeX 写完后期修改方便。
- **draw.io**(现 diagrams.net):架构图 / 流程图白嫖。
- **Affinity Designer**(便宜于 Illustrator):个人买断。
- **科学配色**:
  - **cmocean**:https://matplotlib.org/cmocean/,colormaps(海洋学验证)
  - **viridis**:matplotlib 内置,色觉友好
  - **color brewer**:https://colorbrewer2.org/,离散 / 顺序 / 双向各类

## 9. AI / LLM 工具(2025-26 实际工作流)

- **vLLM**:本地 / 服务端 high-throughput 推理。我的笔记本上跑 7B 模型用这个。
- **Ray**:分布式训练 / 推理调度。
- **HuggingFace Transformers + Datasets**:研究 baseline 的原语。
- **trl**(HuggingFace):SFT / DPO 训练。
- **wandb**:实验追踪。

> 这些更多是 [HANDS ON LLM 笔记](/blog/hands-on-llm/) 的内容,不是这条目重点。

## 10. 个人学习路径(本科生起步)

我是这样走过来的(节选),可以参考:

```
学期初                     → 找方向、看 CS231n / 离散数学打基础
学期中                     → 上 cs231n / CS224N 课,跟课上的 paper list
学期末或寒假                → 选 1 个能上手的方向(GNN / 单细胞 / NLP 子任务),跑通 baseline
暑假                       → 跟实验室 / 实习做点真东西
之后的学期                   → 跟导师做课题,出第一篇 workshop / arxiv
```

**重点:** 不赌方向,赌"**做出来**"。**先复现一个能跑的版本**,想 5. 论文怎么写 比 1. 想法从哪来 重要得多。

## 11. 一些"我现在改用 X 不再用 Y"的心得

- ~~Paper Reading List~~:很多人用,但维护成本高,我现在用 Zotero + 自动同步就够。
- ~~Endnote~~:收费,Zotero 替代即可。
- ~~Mendeley~~:被 Elsevier 收购后变 push 论文阅读,我改用 Zotero + Hypothesis。
- 论文分享会:别流水账,**每周 3 篇**最合适,深读一篇 + 速览两篇。
- 邮件订阅:控制 1-3 个就够,**别天天跳出半成品**。

## 12. 一个真实的"找 idea"案例(我的方向)

想"AI4bio / 单细胞 GRN 推断"作为我的方向时,我用了这样的顺序:

1. **三周读 survey**:scRNA-seq / GRN inference / foundation model 各一篇代表性综述。
2. **本地复现 BEELINE**:在 CNA / mESC / hESC 三个数据上跑 GENIE3 / GRNBoost2 / PIDC,确认我对结果有直感。
3. **记录所有"不对劲"**:跨数据 / 跨指标的方法排名不一致;某些方法在小数据集 / 大数据集表现反着;sklearn 默认配置和论文报告的设置不一样;**BEELINE 的稳态 vs 时变基线不一致**。
4. **找一个"问得清楚"的问题**:Beeline 的 leaderboard 到底多可靠?在不同预处理下方法排名变化多大?
5. **做最小复现 + 加一个图表**:把 README 跑一遍,补一个我自己的"数据扰动 vs 方法排名" 实验。
6. 把这五个步骤写成一份 draft,给自己 / 给老板 / 给可能的合作者看。

> 这个 workflow 我写在 [AI4bio 转折点](/blog/ai4bio-turning-point/) 的"具体怎么入手"小节里。

## 13. 我没在用但值得收藏

- **TopGeek 学术导航**(国内资源集成):https://www.topgeek.org/ ,聚合搜索。
- **Socratic Open Access**(OCR 论文搜索):https://www.semanticscholar.org/ ,语义级搜索。
- **OpenAlex**:https://openalex.org/ ,开放引文数据,可做 trend 分析。
- **Connected Papers / Inciteful**:同上思路。
- **Elicit**(https://elicit.com/):AI 读 paper + 抽取结构化结果,问答式。

---

最后一句:**工具是地图,不是终点**。多花时间在读 paper + 复现 + 跟同行聊,工具只在你决定要做什么之后才有意义。

原文链接(部分转载自 CSDN):
- 常用资源集合 — https://blog.csdn.net/u013648063/article/details/122048461
