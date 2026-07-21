# Sky Huang · Academic Site

> Personal academic website for **Sky Huang (黄思凯)** — built with
> [Hugo](https://gohugo.io/) + [Hugo Blox Kit](https://hugoblox.com/) (the
> successor to the Hugo Academic / Wowchemy theme, used by 150k+ academics).

🔗 **Live site:** <https://tudu1223.github.io/>

---

## 1. About the site

- **Default language:** 简体中文 (`zh-cn`) — UI strings provided by Hugo Blox's i18n bundles.
- **Secondary language scaffold:** English (`en`) — language switcher is wired; the `content/en/` mirror is reserved for forthcoming translations.
- **Theme:** Tailwind CSS v4 (auto-compiled by Hugo), dark / light / system mode, multiple color packs selectable from the navbar.
- **Content sections:**
  - `content/authors/sky-huang/` — author profile (used by the homepage hero).
  - `content/_index.md` — homepage widgets (Biography → Research → Publications → Recent Posts → Contact).
  - `content/blog/<slug>/index.md` — blog posts, page bundles.
  - `content/publications/` — publication records (placeholder; add items as you go).
- **Tag taxonomy:** `tags/Course Notes`, `tags/Research Notes`, `tags/Tools`, plus topical tags (LLM, CS231n, GRN, MATLAB, …).

## 2. Local development

### Prerequisites
- Windows / macOS / Linux
- [Scoop](https://scoop.sh/) (Windows) — used to install the toolchain:
  ```bash
  scoop install hugo-extended go nodejs-lts
  ```
  *Hugo ≥ 0.162 (Extended) is recommended; Go ≥ 1.23 is needed for module downloads; Node.js 20+ for Tailwind / Pagefind.*

### One-time setup
```bash
pnpm install           # Tailwind v4 + pagefind
hugo mod tidy          # pull Hugo Blox modules from go.mod
```

### Daily workflow
```bash
hugo server                    # http://localhost:1313 with live reload
# or
hugo server --buildDrafts      # also render draft posts
```

### Add a new blog post
```bash
hugo new content blog/my-slug/index.md
```
Then edit the front-matter:
```yaml
---
title: "Your title"
summary: "Optional one-liner for cards."
date: YYYY-MM-DD
authors:
  - sky-huang
tags:
  - Course Notes        # or: Research Notes, Tools
  - <topic-tag>
---
```

### Add a publication
```bash
hugo new content publications/my-paper/index.md
```
Follow the schema at <https://docs.hugoblox.com/reference/publications/> —
front-matter supports `publication_types`, `peer_reviewed`, `license`,
`abstract`, `links`, etc.

## 3. Production build

```bash
hugo --gc --minify
```
The static site is written to `public/`.

## 4. Deployment

Deployment to **GitHub Pages (User Pages)** is fully automated by
`.github/workflows/deploy.yml`:

1. Push to `main` of `https://github.com/tudu1223/tudu1223.github.io`.
2. GitHub Actions runs the workflow:
   - installs `hugo-extended 0.162.0`, `pnpm`, and Go;
   - runs `pnpm install`, `hugo mod tidy`, `hugo --gc --minify`;
   - uploads `public/` as a Pages artifact and deploys it.

⚠️ **Important:** the Hugo project files live in this repo (`D:\bloh\blog`).
The actual *User Pages* deployment uses the same `main` branch — the
`deploy.yml` workflow builds the site and publishes `public/` *without*
committing `public/` to the repo. Old hexo-specific files were moved into
`_legacy-hexo/` and are excluded by `.gitignore`.

## 5. Customising the site

| What | Where |
|------|-------|
| Site name, tagline, description | `config/_default/params.yaml` → `hugoblox.identity` |
| Theme colors / fonts | `config/_default/params.yaml` → `hugoblox.theme`, `hugoblox.typography` |
| Navigation | `config/_default/menus.yaml` |
| Languages | `config/_default/languages.yaml` |
| Homepage widgets | `content/_index.md` |
| Author profile | `data/authors/sky-huang.yaml` |
| Blog taxonomy | front-matter `tags:` on each post |

## 6. Project structure

```
.
├── .github/workflows/deploy.yml      # GH Pages CI
├── archetypes/                       # `hugo new` templates
├── assets/                           # processed by Hugo (Tailwind etc.)
├── config/_default/                  # main Hugo + Blox config
│   ├── hugo.yaml
│   ├── languages.yaml
│   ├── menus.yaml
│   ├── module.yaml                   # Hugo module imports
│   └── params.yaml                   # site identity / theme / typography
├── content/
│   ├── _index.md                     # homepage widget blocks
│   ├── authors/sky-huang/_index.md
│   ├── blog/                         # blog posts (page bundles)
│   └── publications/                 # publication entries
├── data/authors/sky-huang.yaml       # profile details
├── go.mod                            # Hugo Blox module deps
├── hugoblox.yaml                     # project metadata
├── layouts/                          # local overrides (mostly empty)
├── package.json                      # pnpm scripts
├── pnpm-lock.yaml
└── _legacy-hexo/                     # ⚠️ archived hexo project — gitignored
```

## 7. Migrating from the old Hexo blog

The previous Hexo site (`anzhiyu` theme, ~31 posts) was archived into
`_legacy-hexo/`. Posts were triaged as follows:

- **Kept and migrated** (5 posts, retagged):
  - `hands-on-llm/` — *Research Notes · LLM*
  - `cs231n-notes/` — *Course Notes · CS231n*
  - `discrete-math-foundations/` — *Course Notes · Mathematics*
  - `matlab-colors-and-plots/` — *Tools · MATLAB*
  - `research-resources/` — *Tools · Academic Writing*
- **Archived (not migrated)** in `_legacy-hexo/source/_posts/` — CTF/pwn
  write-ups, install guides, and procedural notes. These are still on disk
  if you want to recover any of them, but they will not appear on the new
  site.

If you ever want to bring a legacy post back, copy the `.md` body into a
new `content/blog/<slug>/index.md` and add Hugo front-matter.

---

> ✍️ "研究阶段主线: 单细胞转录组学 · 基因调控网络推断 · 多组学整合 · AI4Science 基准构建。"
