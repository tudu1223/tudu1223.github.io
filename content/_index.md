---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2026-07-21
type: landing

sections:
  # === Hero / Biography ===
  - block: resume-biography-3
    content:
      username: sky-huang
      text: ''
      headings:
        about: 'About'
        education: 'Education'
        interests: 'Research interests'
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle

  # === Research statement ===
  - block: markdown
    content:
      title: '🔬 Research'
      subtitle: 'AI for Science, single-cell & GRN inference'
      text: |-
        **Research focus.** I focus on **single-cell transcriptomics** and **gene regulatory
        network (GRN) inference**. By integrating multi-omics data and high physical-confidence
        evidence, I build principled algorithms and rigorous benchmarks for GRN inference,
        aiming to make the results both biologically meaningful and computationally reproducible.

        I am broadly interested in **AI for Science (AI4Science)**: how scientific priors
        (physics, biology, structure) can guide machine learning, and how benchmarks can
        expose what current methods actually generalize to.

        **研究方向。** 围绕单细胞转录组学与基因调控网络（GRN）推断展开；结合多组学与
        高物理置信度数据，做算法构建与精准基准评估，让结果既在生物学上可解释、又能
        在计算上可复现。
    design:
      columns: '1'

  # === Featured publications (placeholder) ===
  - block: collection
    id: papers
    content:
      title: 'Featured Publications'
      text: 'No featured publications yet — section reserved for forthcoming work.'
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: '2'

  # === Recent publications (placeholder) ===
  - block: collection
    content:
      title: 'Recent Publications'
      text: ''
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation

  # === Recent posts ===
  - block: collection
    id: news
    content:
      title: 'Recent Posts'
      subtitle: 'Notes on research, methods, and the AI4Science reading path.'
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
        padding: [0, 0, 0, 0]

  # === Contact / further reading ===
  - block: markdown
    content:
      title: '📬 Get in touch'
      subtitle: ''
      text: |-
        I am open to research collaboration, paper discussions, or simply chatting about
        AI4Science and single-cell methods. The fastest way is e-mail:

        ✉️ **sk_hwong@outlook.com**

        For code and notes, see [GitHub](https://github.com/tudu1223) and
        [ORCID](https://orcid.org/0009-0003-2335-563X).
        Long-form Chinese notes also live on my WeChat public account
        **「江水的云组会」**.
    design:
      columns: '1'
---
