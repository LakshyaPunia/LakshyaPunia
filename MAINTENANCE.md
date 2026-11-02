# Maintaining the analytics engineering profile

Publish this repository publicly as `LakshyaPunia/LakshyaPunia` to display the README on the profile.

## Content

Edit the introduction, skill bullets and project table in `README.md`. Workplace-specific tools should be added only after Lakshya confirms them. The current selection reflects his stated analytics engineering role and public project evidence.

## Animation

`python scripts/build_intro.py` generates the original light/dark GIF subtitles, PNG stills and SVG tool labels. It requires Pillow. The default font is Segoe UI on Windows; set `PROFILE_BODY_FONT` to another installed TrueType font if needed.

The README selects light/dark sources and requests a still for reduced-motion preferences. Rendering support can vary. All essential role, skills and project information is also readable Markdown text. The old photographic assets are removed; the previous version remains in Git history.

## Daily refresh

`.github/workflows/refresh-profile.yml` refreshes the compact public-project count daily or manually through Actions. It uses the automatic repository token and standard-library Python, with no paid service or personal token.

`python scripts/update_profile.py` runs the same update locally. Keep exactly one pair of `ACTIVITY:START` and `ACTIVITY:END` markers. The count excludes private repositories, forks and the profile itself. If the API fails, the README stays unchanged.

GitHub can delay scheduled runs and can disable schedules after 60 days of repository inactivity. The hosted workflow must be verified after publication.

## Preview

`python scripts/preview.py` creates `preview.html` using markdown-it-py. This approximates GitHub styling; the published GitHub rendering is authoritative. Preview files are excluded from Git.
