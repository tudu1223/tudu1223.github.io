# AGENTS.md — Project context for any agent working on this blog

> Read this file first if you've been asked to update or modify the blog.
> It collects everything that took hands-on time to learn, so you don't
> have to re-learn it. Keep it updated as the project evolves.

---

## 0. TL;DR

This is the personal academic website of **Sky Huang (黄思凯)**, an
undergraduate researcher at Fujian Agriculture and Forestry University.
It's hosted at <https://tudu1223.github.io/> and rebuilt from this repo
on every push to `main` via GitHub Actions.

**Stack:**

```
Hugo (Extended) ──► Hugo Blox Kit 0.12 (theme + builder)
              └──► Tailwind CSS v4 (compiled at build time)
              └──► Pagefind (search index)
Default content language: zh-cn (Simplified Chinese) with English fallback.
```

**Brand voice:** academic, restrained, technical, opinionated. No marketing copy.

---

## 1. The person behind the site

| Field | Value |
|---|---|
| 中文名 | 黄思凯 |
| 英文名 / 显示名 | **Sky Huang** |
| 角色 | Undergraduate (在读) |
| 单位 | 福建农林大学 (FAFU) |
| 研究方向 | AI4Science — single-cell transcriptomics + gene regulatory network (GRN) inference |
| 邮箱 | `sk_hwong@outlook.com` |
| ORCID | `https://orcid.org/0009-0003-2335-563X` |
| GitHub | `tudu1223` (default; assumed matching `tudu1223.github.io`) |
| 公众号 | 江水的云组会 (no public URL yet — placeholder) |
| 拼音 | Huáng Sīkǎi, he/him |

The author profile (used by the homepage hero + every blog post byline)
lives at **`data/authors/sky-huang.yaml`**. **Always edit that file** if
you need to change name, role, links, bio, education, experience,
skills, languages, awards, or interests.

> The short bio in `bio:` (also in that YAML) is what fills the
> "About" section on the homepage hero. Keep it bilingual (English
> first, then Chinese). Current bio is ~1100 chars total.

---

## 2. Repo layout

```
D:\bloh\blog\
├── .github/workflows/deploy.yml   ← GH Pages CI (hugo + pnpm + npm install)
├── .nojekyll                     ← disables GH Pages' default Jekyll renderer
├── .gitignore                    ← excludes public/, node_modules/, _legacy-hexo/
├── AGENTS.md                     ← you are here
├── README.md                     ← (gone — moved to docs/README.md)
├── docs/README.md                ← old README, kept for reference, not served
├── _legacy-hexo/                 ← ⚠️ OLD Hexo+anzhiyu project, gitignored
│                                    Contains 31 original posts & assets.
│                                    DO NOT edit anything here. Treat as read-only
│                                    archive of the previous incarnation.
│
├── assets/css/                   ← only main.css lives here (custom.css was deleted)
├── config/_default/              ← 5 Hugo config files (see §3)
├── content/
│   ├── _index.md                 ← homepage widget list
│   ├── authors/sky-huang/_index.md
│   ├── blog/                     ← blog posts (page bundles)
│   │   ├── ai4bio-turning-point/ ← newest depth article
│   │   ├── hands-on-llm/
│   │   ├── cs231n-notes/
│   │   ├── discrete-math-foundations/
│   │   ├── matlab-colors-and-plots/
│   │   └── research-resources/
│   └── publications/             ← publications section (currently empty placeholder)
│
├── data/authors/sky-huang.yaml   ← author profile (single source of truth)
├── hugoblox.yaml                 ← project metadata for Hugo Blox
├── hugo.yaml / hugo.toml         ← Hugo runtime config (created by `hugo new site`)
├── go.mod / go.sum               ← Go module manifest for Hugo Blox imports
├── package.json / pnpm-lock.yaml ← Tailwind v4 + Pagefind runtime
├── netlify.toml                  ← left over from template, unused
├── themes/                       ← intentionally empty (we use Go modules, not git submodules)
├── layouts/                      ← local layout overrides (kept empty for now)
├── static/uploads/               ← static file uploads (e.g. CV pdf, future images)
├── i18n/                         ← language bundles
└── archetypes/                   ← `hugo new` templates (only default.md currently)
```

---

## 3. Config files (under `config/_default/`)

| File | Purpose | Do not edit unless… |
|---|---|---|
| `hugo.yaml` | Base Hugo config (`baseURL`, `defaultContentLanguage`, build flags) | changing URL, language, advanced behavior |
| `languages.yaml` | Multi-lang scaffold; currently only `zh-cn` is enabled, `en` is commented out as future scaffold | adding a real third language, or switching the default |
| `menus.yaml` | Top navbar (`main` enum). Currently 4 items: Bio / Publications / Posts / Publications Archive | adding/removing nav items |
| `module.yaml` | Hugo Blox Go-module imports (`blox`, `integrations/netlify`, `slides`). **Do not touch** without reason | bumping module versions |
| `params.yaml` | **Site identity** (`hugoblox.identity.name`, tagline, description), theme, typography, header behaviour. **This is the most likely file to edit for visual / branding changes.** | changing colors / fonts / layout density / header style |

The root `hugoblox.yaml` is for **project metadata** (hugo_version, deploy
host, template id). It is not the primary config — Hugo reads it as a
secondary source.

---

## 4. Content conventions

### 4.1 Frontmatter

**Posts** use this minimal Hugo Blox-compatible frontmatter (YAML):

```yaml
---
title: "My post"
summary: "One-liner for cards & SEO."
date: "2026-02-01"
authors:
  - sky-huang
tags:
  - Research Notes     # one of: Course Notes / Research Notes / Tools / Method Notes / Opinion
  - <topic-tag>
categories:
  - research-notes     # matches a tag category below
---
```

**Author profile** (data/authors/sky-huang.yaml) uses the Hugo Blox
schema v1 (see top of file for `schema:` line).

### 4.2 Tag taxonomy

Top-level tags are restricted to these **four type labels** —
use them on every post:

| Tag | When |
|---|---|
| `Course Notes` | 学习某门课的笔记 / cs231n / 离散数学 |
| `Research Notes` | 我正在研究 / 复现 / 思考的东西 / HANDS ON LLM / AI4bio |
| `Tools` | 资源 / 教程 / 实用工具 / MATLAB / 科研网址 |
| `Opinion` | 立场稿 / 反思类 / 公开判断 (e.g. AI4bio 转折点) |
| `Method Notes` | 写某个具体方法的笔记 (e.g. QLoRA 笔记、BEELINE 复现笔记) |

Then add **subject-specific tags** freely:
`LLM`, `Hands-on`, `Computer Vision`, `Deep Learning`, `CS231n`,
`Mathematics`, `Foundations`, `Visualization`, `MATLAB`,
`Academic Writing`, `Resources`, `AI4Science`, `GRN inference`,
`Single-cell`, etc.

The `categories:` field should mirror one of the four primary tags.

### 4.3 Posts structure

Each post lives in `content/blog/<slug>/index.md` as a **page bundle**
(add images etc. as siblings of `index.md` if needed; current posts
have no extra assets).

**Slug rules:** lowercase, ASCII or pinyin only, words separated by `-`.
Examples: `hands-on-llm`, `cs231n-notes`, `ai4bio-turning-point`.

### 4.4 Homepage widgets

`content/_index.md` is the **landing-page widget list**. Each entry is
a Hugo Blox block; the blocks we use today:

1. `resume-biography-3` — Hero (name + role + social + bio + interests)
2. `markdown` — Generc content (Now, Research, Contact, etc.)
3. `collection` — Blog aggregation (Recent Posts)

`config/_default/menus.yaml` and `content/_index.md` are interlocked: any
ID set on a `collection` block (`id: news`, `id: papers`) can be linked
from `menus.yaml` with `/#news` style URLs.

### 4.5 Bilingual scaffold

- **Default content language:** `zh-cn` (Simplified Chinese).
- **English** is scaffolded (commented out in `languages.yaml`) but has
  no `content/en/` mirror — so the site UI is in Chinese, the theme
  strings mix Chinese with theme-packs that English can render.
- When adding English content, uncomment the `en:` block in
  `languages.yaml` and place English posts under `content/en/`.

### 4.6 Academic bibliography style

For in-post links and bibliography, the project uses **`reference.csl`**
embedded by Hugo Blox's `pub-` blocks. The `ai4bio-turning-point` post
shows the working pattern (DOI + URL fallback).

---

## 5. Author profile & contact details

**Single source of truth:** `data/authors/sky-huang.yaml`.

If the user tells you their role changed (e.g. became Master's student),
edited email, or added a publication type — **edit only this file**.
Other files (`content/_index.md`, `content/authors/sky-huang/_index.md`,
`hugoblox.yaml`, `config/_default/params.yaml`) reference these values.

`content/authors/sky-huang/_index.md` is the cascade/index file for the
author profile page. Currently it just declares `title` + `slug` — the
heavy data lives in `data/authors/sky-huang.yaml`.

---

## 6. Build / dev / deploy workflow

### 6.1 Local dev

Prerequisites: **Hugo Extended ≥ 0.160** (currently pinned to 0.160.1 in
deploy.yml). Other versions **may break CSS**. See §8 for the 0.162 story.

```bash
cd D:\bloh\blog
hugo server --buildDrafts          # http://localhost:1313 with live reload
```

### 6.2 Production build

```bash
hugo --gc --minify
```

Outputs to `public/`, which is gitignored (CI builds fresh). Never
commit `public/`, `resources/`, `hugo_stats.json` — these are build
artifacts that drift between local and CI.

### 6.3 Node.js deps

```bash
# EITHER pnpm install (recommended locally)
pnpm install

# OR npm install (used in CI; works equally well for our deps)
npm install
```

Hugo Blox compiles Tailwind v4 at build time, so deps must be installed
**before** `hugo --gc --minify` for CSS to appear in `public/`.

### 6.4 GitHub Pages CI

`.github/workflows/deploy.yml` runs on every push to `main`:

1. `actions/checkout@v4` (no submodules — we use Go modules)
2. `actions/setup-go@v5` (Go 1.23)
3. `actions/setup-node@v4` (Node 20)
4. `peaceiris/actions-hugo@v3` (Hugo 0.160.1 Extended)
5. `npm install` — Tailwind v4 + pagefind
6. `hugo --gc --minify --printPathWarnings`
7. `actions/upload-pages-artifact@v3` (uploads `./public`)
8. `actions/deploy-pages@v4` (deploys the artifact)

**CRITICAL:** GitHub Pages Source must be set to **"GitHub Actions"**
(not "Branch: main"). If it ever flips back, the site returns to
serving the branch directory, which used to mean a Jekyll-rendered
fallback. The repo now has `.nojekyll` at root and inside `public/` to
prevent that, but the **artifact** still won't publish unless Source is
"GitHub Actions".

---

## 7. Common tasks — quick recipes

### 7.1 Add a new blog post

```bash
# mkdir + cd into the slug
mkdir content/blog/<slug>
```

Write `content/blog/<slug>/index.md`:

```yaml
---
title: "..."
summary: "..."
date: YYYY-MM-DD
authors:
  - sky-huang
tags:
  - Research Notes
  - <topic tag>
categories:
  - research-notes
---
```

Frontmatter auto-populates: cards in `Recent Posts`, RSS feed,
search index. Nothing else to wire up.

### 7.2 Update author bio / role / email

Edit `data/authors/sky-huang.yaml` — that's the single source of truth
for everything visible on the homepage hero.

### 7.3 Change site name / tagline / description

Edit `config/_default/params.yaml` → `hugoblox.identity`.

### 7.4 Add a new top-nav item

Edit `config/_default/menus.yaml`. The URL can be:
- `/#<id>` — links to a homepage collection block with matching `id`
- `/<section>/` — links to a Hugo section (e.g. `publications/`)

### 7.5 Change theme color (default indigo, etc.)

Edit `config/_default/params.yaml` → `hugoblox.theme.colors`. Use a
Tailwind palette name (`indigo`, `rose`) or a hex (`#6366f1`).

### 7.6 Disable the gradient mesh / background on hero

Edit `content/_index.md` first block:

```yaml
design:
  background:
    gradient_mesh:
      enable: false
```

### 7.7 Adjust hero side-padding / container width

Edit `assets/css/main.css`. The `@layer base { [class~="max-w-7xl"] }`
rule widens the landing container from 80rem → 96rem.

### 7.8 Force-bust CDN / browser cache

The pipeline renames CSS files to hashed names on every build, so any
push forces a fresh CSS fetch. But if the user reports an issue:
have them `Ctrl+Shift+R` or open in incognito.

---

## 8. Things NOT to repeat (lessons)

These cost real time. They are why they are written down.

### 8.1 Don't ship a CSS file at `assets/css/custom.css` alongside `assets/css/main.css`

Hugo emits **both** as `custom.min.<hash>.css` + `entry.<hash>.css`. The
custom file gets loaded in addition to the main one and rules inside
will override (or get overridden) unpredictably. **Pick one entry
file** — we now use `main.css` only.

If you see a layout bug that looks like an old rule taking effect, look
in `assets/css/` for a second file.

### 8.2 Don't put `README.md` at repo root if you want GH Actions deploy

GitHub Pages automatically renders any `.md` at the root of a branch
served as Pages. If Pages Source is `Branch: main`, the README shows
up at `/`. Even if Source is "GitHub Actions", sometimes Settings
reset. **Always have:**

- `.nojekyll` at repo root
- `.nojekyll` inside `public/` (so the deployed artifact also disables
  Jekyll)
- `README.md` outside the root if you want to keep one for the repo
  itself — we put ours at `docs/README.md`.

### 8.3 Pin Hugo to 0.160.x, not 0.162+

Hugo 0.162 changed the `css.TailwindCSS` sandbox configuration. Hugo
Blox 0.12 + Tailwind v4 fails the `Build with Hugo` step on 0.162
locally but works on 0.160.1. The CI workflow pins to 0.160.1.

If upgrading is needed later, the path is probably:
1. Bump the blox module to a newer minor first.
2. Test `css.TailwindCSS` behaviour on a sample content locally.
3. Then update both the workflow *and* local scoop.

### 8.4 Don't `pnpm mod tidy` in CI

`hugo mod tidy` rewrites go.mod / go.sum to the latest compatible
modules, which can pull a Hugo Blox minor release that doesn't match
the assets the rest of the site expects. The CI never runs `hugo mod
tidy`; the modules are pinned via the committed `go.mod` and pulled by
`peaceiris/actions-hugo` indirectly.

### 8.5 Don't rely on `pnpm/action-setup` alone

The very first CI run failed because `pnpm install --frozen-lockfile`
couldn't find `pnpm` in PATH. Cause: `actions/setup-node@v4` with
`cache: 'pnpm'` resolves a cache key but doesn't actually install
pnpm. Workaround: use `npm install` directly (works the same for
Tailwind v4), or `npm install -g pnpm@10`. We chose `npm install`.

### 8.6 GitHub Pages Source must be "GitHub Actions"

If the live site stops showing Hugo output and goes back to a 14 KB
Jekyll-rendered README, go to
<https://github.com/tudu1223/tudu1223.github.io/settings/pages> and set
Source to **GitHub Actions**. Then `Actions: deploy` runs on the next
push.

### 8.7 Don't commit `public/`, `resources/`, `hugo_stats.json`

The CI regenerates them. Stale copies in git confuse diagnosis because
they look like a cached artifact.

### 8.8 Don't leave hidden CSS rules active

Earlier an old `assets/css/custom.css` contained `display:none` for the
left hero column. Even after the source file was conceptually "removed",
the file persisted on disk and was bundled into every deploy. **Verify
that ANY rule you think you've removed is actually removed from BOTH
the source file and the rendered output** (`grep` the live site's CSS).

---

## 9. Verification checklist before any "all done"

```bash
# 1. Build succeeds
hugo --gc --minify

# 2. Local preview shows intended change
hugo server --buildDrafts          # open localhost:1313

# 3. CSS file hash in build is fresh
ls public/css/ | sort

# 4. No stale CSS file lingers
grep -oE '/css/custom[^\"]*\.css' public/index.html  # should be empty

# 5. Content fields the user cares about are present
grep -E "Sky Huang|Huáng Sīkǎi|outlook.com" public/index.html

# 6. Commit + push
git add -A
git commit -m "<what changed>"
git push origin main

# 7. Watch CI
# https://github.com/tudu1223/tudu1223.github.io/actions

# 8. Confirm live
curl -s https://tudu1223.github.io/ | head -c 200
# should see "<title>Sky Huang</title>" or similar
```

---

## 10. Custom CSS contract — read this before editing `assets/css/main.css`

```css
@layer base {
  .resume-biography { padding: ... }              /* hero vertical spacing */
  .resume-biography .prose,
  .resume-biography .prose-lg { max-width: none } /* fill col-span-8 with text */
  [class~="max-w-7xl"] { max-width: 96rem }        /* wider landing container */
}

@layer utilities {
  .hb-section-spacing { ... }
}
```

**Rules:**

- Use Tailwind v4 `@layer base` for project-level overrides.
- Use `[class~="..."]` attribute selectors (not `[class*="..."]`) — the
  former matches whole-token classes; the latter matches substrings
  and may collide with utility classes.
- `!important` is acceptable on overrides — Hugo Blox utility classes
  also use `!important` so we need the bump.

---

## 11. Public URLs

| URL | What |
|---|---|
| <https://tudu1223.github.io/> | Production site (Hugo, deployed by Actions) |
| <https://github.com/tudu1223/tudu1223.github.io> | Repo |
| <https://github.com/tudu1223/tudu1223.github.io/settings/pages> | Pages source configuration (set to "GitHub Actions") |
| <https://github.com/tudu1223/tudu1223.github.io/actions> | CI runs |
| <https://orcid.org/0009-0003-2335-563X> | Sky Huang's ORCID |
| <mailto:sk_hwong@outlook.com> | Sky Huang's contact |

---

## 12. Style + voice notes for the user-facing prose

- **No marketing tone.** "Capture attention", "Get Started", "transform
  your X" — not on this site.
- **Bilingual posture.** If you write Chinese, mirror it in English
  (longer), not the other way around.
- **Citations > opinions without backing.** When claiming a method's
  rank is unstable on BEELINE, cite the specific methods, give the
  numbers if you have them, and link the papers.
- **Disagreement is OK.** The homepage About, the hero column, the
  AI4bio post all stake out specific positions. Don't soften them
  into neutral mush.
- **Match the academic standard, not the markdown-blog standard.**
  Use katex-style equations (`$L = ...$`) where they earn their keep.

---

## 13. Change log

- **2026-07-21** — Project initialised. 31 hexo posts archived into
  `_legacy-hexo/`. 5 substantive posts migrated & retagged
  (Course Notes / Research Notes / Tools), 1 in-depth piece on
  AI4bio turning point added (`ai4bio-turning-point`).
- **2026-07-21** — Hugo Blox layout switched from default 3-col hero to
  single-column `markdown` hero after the user feedback "needs more
  content density, no avatar". Switched back to two-column hero after
  second feedback. Container widened to 96rem, prose `max-width: none`
  applied so text spans the col.
- **2026-07-21** — `.nojekyll` added; `README.md` moved to `docs/`. CSS
  rogue `assets/css/custom.css` deleted. Live now consistently returns
  ~117 KB Hugo HTML, not 14 KB Jekyll.
- **2026-07-21** — Author bio expanded to ~1100 chars (turning-point
  framing; "AI4bio at a turning point" + wet-lab-actionable pipeline;
  removed "本科起步，节奏稳一点" per request).
- **2026-07-21** — All 5 migrated posts expanded to ~1000–2000 words.
  AI4bio turning-point depth article added.

---

## 14. Quick references

| Question | Where to look |
|---|---|
| How do I update Sky Huang's bio? | `data/authors/sky-huang.yaml` |
| How do I add a new homepage section? | `content/_index.md` |
| How do I change site colors? | `config/_default/params.yaml` (`hugoblox.theme.colors`) |
| How do I fix a layout bug? | Start with `assets/css/main.css` rule + check `public/css/` for hash + check §8.1 |
| Why is the site showing Jekyll output? | §8.2; check `.nojekyll` exists and Pages Source = "GitHub Actions" |
| Why is the build failing on CI? | Run `hugo --gc --minify` locally first; check `hugo_stats.json` gitignore; confirm Hugo version matches 0.160.1 in `deploy.yml` |
| How do I deploy? | Just push to `main`. Workflow handles the rest. |
