# JoongWon Shin — Academic Portfolio

Personal academic portfolio built with Jekyll and the Signal archive/CV engines. Profile text, archive entries, publications, and CV cells are maintained as Markdown or YAML; shared Liquid components generate the page HTML.

## Content architecture

```text
.
├── _config.yml                  # Site URL, collections, defaults, and contacts
├── _data/
│   ├── profile.yml              # Home profile and research-interest content
│   ├── navigation.yml           # Top-navigation order and labels
│   ├── content_archives.yml     # Archive source, grouping, and row type
│   ├── content_groups.yml       # Category order and display labels
│   └── cv_sections.yml          # CV section order and headings
├── _pages/                      # Thin page definitions and public permalinks
├── _experiences/                # Experience entries
├── _posts/                      # Dated note entries
├── _publications/               # Publication entries
├── _cv/                         # Reusable CV cells
├── _layouts/                    # Shared page and archive rendering
├── _includes/                   # Shared rows, CV cells, header, and footer
├── assets/
│   ├── css/signal.scss          # Responsive visual system
│   ├── js/signal.js             # Filters and interactions
│   └── cv.pdf                   # Downloadable CV
└── .github/workflows/pages.yml  # GitHub Pages deployment
```

The generation path is:

1. Markdown supplies entry content and metadata.
2. `_data/*.yml` defines navigation, archive behavior, category order, and CV order.
3. Thin files in `_pages/` bind a public URL to a stable `key`.
4. `_layouts/signal-collection.html` groups and sorts entries, then dispatches each row through `_includes/signal-content-row.html`.
5. `signal.scss` and `signal.js` provide the responsive layout and interaction layer.

## Update the home page

Edit `_data/profile.yml` for the visible name, introduction, profile image, and the three research interests. Contact links come from `author.email` and `author.github` in `_config.yml`.

The newest Experience and Note entries are selected automatically for the home-page previews.

## Add an Experience or Note

Experiences and Notes use the same general row schema. Experiences live in `_experiences/`; Notes use dated files in `_posts/` and set `key: notes`.

```yaml
---
title: "Entry title"
date: 2026-01-01
key: notes          # leave empty for _experiences entries
period:             # optional custom date label
category: "project"
organization:
summary: "One concise archive-row description."
thumbnail:          # optional; the same row adapts when present
link:               # optional override; defaults to the generated detail URL
---
```

Category section names and ordering are defined in `_data/content_groups.yml`. A new category must be added there before it appears in a category-grouped archive.

## Add a Publication

Create one Markdown file in `_publications/`:

```yaml
---
layout: single
title: "Paper title"
date: 2026-01-01
category: "conference"
venue: "Conference or journal"
paperurl: "https://example.com/paper"
highlight: "Optional note, award, or presentation type."
thumbnail_label: "SHORT LABEL"
primary_author: "JoongWon Shin"
authors:
  - "JoongWon Shin"
  - "Collaborator Name"
---
```

Year sections and category filter buttons are derived automatically from `date` and `category`. No archive HTML needs to be edited.

## Update the CV

CV section order and labels live in `_data/cv_sections.yml`. Each file in `_cv/` belongs to one section and selects one reusable cell:

- `template: entry` — heading, link, period, subtitle, facts, note, and Markdown body.
- `template: pairs` — compact label/value lists for coursework and skills.

Multiple cells can share one `section`; their `order` values control placement and they are separated by compact spacing rather than new timeline markers.

```yaml
---
section: education
template: entry
order: 20
heading: "Degree or institution"
period: "2026 – Present"
subtitle: "Program or role"
---

Optional Markdown details.
```

The timeline line, marker position, and violet–blue–cyan marker colors are generated automatically. Replace `assets/cv.pdf` when the downloadable PDF changes.

## Add or reconfigure an archive

An archive joins four files through one stable `key`:

- `_pages/<page>.md` — title, permalink, and key;
- `_data/content_archives.yml` — source, grouping mode, and row family;
- `_data/content_groups.yml` — category groups when `group_by: category`;
- `_data/navigation.yml` — optional top-navigation entry.

The permalink remains independent from the key. Navigation resolves the matching page by key and uses that page's current URL.

## Local verification

```bash
bundle install
bundle exec jekyll serve
```

Open `http://localhost:4000`. A production-equivalent build can be checked with:

```bash
JEKYLL_ENV=production bundle exec jekyll build
```

GitHub Pages deployment is handled by `.github/workflows/pages.yml` on pushes to `main`.

## License and attribution

The code is distributed under the MIT License. Upstream attribution and third-party asset notices are recorded in `LICENSE` and `THIRD_PARTY_NOTICES.md`.
