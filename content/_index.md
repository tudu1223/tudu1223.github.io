---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2026-07-21
type: landing

sections:
  # === Hero / Biography (compact) ===
  - block: resume-biography-3
    content:
      username: sky-huang
      text: ''
      headings:
        about: 'About'
        education: 'Education'
        interests: 'Research interests'
    design:
      # Disable the gradient mesh — it reads as an empty block before any avatar
      background:
        gradient_mesh:
          enable: false
      name:
        size: sm  # smaller heading → less vertical whitespace at the top
      avatar:
        size: small  # 150px — compact for a no-avatar placeholder
        shape: circle

  # === Now (dense highlights strip) ===
  - block: markdown
    content:
      title: 'Now'
      subtitle: ''
      text: |-
        - 🧬 Researching **GRN inference** under the AI4Science umbrella at FAFU.
        - 📚 Building a **benchmark** for single-cell GRN methods with high physical-confidence priors.
        - ✍️ Reading the AI4Science / single-cell literature; notes on the **Posts** page below.
    design:
      columns: '2'

  # === Research statement ===
  - block: markdown
    content:
      title: '🔬 Research'
      subtitle: 'AI for Science · single-cell & GRN inference'
      text: |-
        I focus on **single-cell transcriptomics** and **gene regulatory network (GRN)
        inference**. By integrating multi-omics data with high physical-confidence
        evidence, I build principled algorithms and **rigorous benchmarks** for GRN
        inference, with the goal of making results both biologically meaningful
        and computationally reproducible.

        Broader interest in **AI for Science (AI4Science)**: how scientific priors
        (physics, biology, structure) guide ML, and how benchmarks reveal what
        current methods actually generalise to.

        **研究方向。** 围绕单细胞转录组学与基因调控网络（GRN）推断展开；结合多组学与
        高物理置信度数据，做算法构建与精准基准评估，让结果既在生物学上可解释、又能
        在计算上可复现。
    design:
      columns: '1'

  # === Recent Posts (primary content) ===
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
      # Don't strip padding between cards — the previous zero padding made the
      # strip collapse against surrounding blocks and look disconnected.
      spacing:
        padding: ['1rem', 0, 0, 0]

  # === Publications (inline note; uncomment with real content later) ===
  # - block: collection
  #   id: papers
  #   content:
  #     title: 'Publications'
  #     subtitle: 'Forthcoming. Track work-in-progress on GitHub.'
  #     filters:
  #       folders: [publications]
  #       featured_only: true
  #   design:
  #     view: article-grid
  #     columns: '2'

  # === Contact / further reading ===
  - block: markdown
    content:
      title: '📬 Get in touch'
      subtitle: ''
      text: |-
        Open to research collaboration, paper discussions, or just chatting about
        AI4Science and single-cell methods.

        ✉️ **[sk_hwong@outlook.com](mailto:sk_hwong@outlook.com)** ·
        [GitHub](https://github.com/tudu1223) ·
        [ORCID](https://orcid.org/0009-0003-2335-563X)

        长文中文笔记同步在微信公众号 **「江水的云组会」**。
    design:
      columns: '1'
---
