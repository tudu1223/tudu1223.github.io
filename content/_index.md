---
# Sky Huang · homepage widget list
title: ''
summary: ''
date: 2026-07-21
type: landing

sections:
  # ===========================================================
  # 顶部 hero — 双列布局
  #   左列(占 1/3): 姓名 · 角色 · 单位 · 社交圈
  #   右列(占 2/3): About + 中英简介
  # ===========================================================
  - block: resume-biography-3
    content:
      username: sky-huang
      headings:
        about: 'About'
        education: 'Education'
        interests: 'Research interests'
    design:
      background:
        gradient_mesh:
          enable: false
      name:
        size: lg
      avatar:
        size: small
        shape: circle

  # ===========================================================
  # 当前在做（高密度三段）
  # ===========================================================
  - block: markdown
    content:
      title: 'Now · 在做与在学'
      subtitle: ''
      text: |-
        - 🧬 **Research** — 围绕 *GRN inference* 做算法构造：在多组学 + 高物理置信度
          先验下比较 BEELINE 等基准上的现有方法；目标写一个能严格复现、纯靠 CPU
          也能跑的开源基线。
        - 📚 **Reading** — 推理工 Tang 与 Li 写的 *AI for Science* 综述、单细胞
          foundation model（scGPT、GeneFormer、scBERT）的对照论文，最近同步
          重新过一遍 CS231n。
        - 🧪 **Coursework** — 离散数学（核心基础）、汇编 / 编译原理、机器学习导论、
          概率统计。
        - ✍️ **Notes** — 把上面的内容整理成笔记，写在 *Recent Posts*。
    design:
      columns: '2'

  # ===========================================================
  # 研究陈述（双语完整版）
  # ===========================================================
  - block: markdown
    content:
      title: '🔬 Research · 研究陈述'
      subtitle: 'AI for Science · single-cell & GRN inference'
      text: |-
        I focus on **single-cell transcriptomics** and **gene regulatory network
        (GRN) inference**. By integrating multi-omics data with high physical-
        confidence evidence, I build principled algorithms and **rigorous benchmarks**
        for GRN inference, with the goal of making results both biologically
        meaningful and computationally reproducible.

        I am broadly interested in **AI for Science (AI4Science)**: how scientific
        priors (physics, biology, structure) guide ML, and how benchmarks reveal
        what current methods actually generalise to. As an undergraduate I treat
        this as a long-term direction — preferring to invest in methods that can
        later be plugged into a wet-lab pipeline, not chasing leaderboard wins.

        **研究方向。** 围绕单细胞转录组学与基因调控网络（GRN）推断展开；
        结合多组学与高物理置信度数据，做算法构建与精准基准评估；
        让结果既在生物学上可解释、又能在计算上可复现。本科阶段我把这视为
        长期方向，而不是短期对标榜刷榜。
    design:
      columns: '1'

  # ===========================================================
  # Recent Posts（5 篇笔记）
  # ===========================================================
  - block: collection
    id: news
    content:
      title: 'Recent Posts · 近期笔记'
      subtitle: '研究笔记 / 课程笔记 / 工具单 — 当前共 5 篇'
      text: ''
      page_type: blog
      count: 6
      filters:
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''
      offset: 0
      order: desc
    design:
      view: card
      spacing:
        padding: ['1rem', 0, 0, 0]

  # ===========================================================
  # Contact / 合作入口
  # ===========================================================
  - block: markdown
    content:
      title: '📬 Get in touch · 合作 / 聊聊'
      subtitle: ''
      text: |-
        欢迎就 GRN 推断、单细胞基准、AI4Science 综述、或者单纯想聊聊方法论联系。
        最快的方式是邮件 — 我能及时看到。

        ✉️ **[sk_hwong@outlook.com](mailto:sk_hwong@outlook.com)**
        [GitHub](https://github.com/tudu1223) ·
        [ORCID](https://orcid.org/0009-0003-2335-563X)

        长文中文记录同步推送微信公众号 **「江水的云组会」**。
    design:
      columns: '1'
---
