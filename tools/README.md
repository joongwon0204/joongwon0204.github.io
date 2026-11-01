# Poster source

`build_english_ai_poster.py` recreates the English A0 poster in
`assets/generative-ai-inequality-poster-en.pdf`.

Dependencies: Python 3, `reportlab`, `pypdf`, and `Pillow`.

```sh
python3 tools/build_english_ai_poster.py
pdftoppm -scale-to 3370 -singlefile -png assets/generative-ai-inequality-poster-en.pdf assets/generative-ai-inequality-poster-en
```

The Korean PDF in `assets/` remains the source of record. The English poster
preserves its final survey-chart labels and counts, statistical results, and
six original English-language distribution plots. It does not reconstruct
respondent-level data. Fonts are embedded from ReportLab's bundled Vera files.

Korean Notes originals are preserved under `backups/notes-ko/2026-11-01/`.
Both `tools/` and `backups/` are excluded from the generated website.
