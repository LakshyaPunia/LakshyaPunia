# Maintaining the analytics engineering profile

Publish this repository publicly as `LakshyaPunia/LakshyaPunia` to display the README on the profile.

## Content

Edit the introduction, technical focus bullets, and side-project table in `README.md`. The dbt, Snowflake, automation, IaC, GitHub Actions, PII, agentic coding, cost analysis, and local Tableau MCP details come from Lakshya's direct description of his work. Keep employer system details at the level he has shared publicly.

The featured repositories are personal projects. Keep Vivre described as a prototype with simulated readings. Do not imply the model is clinically validated or that these repositories contain TMRW work.

## Animation

`python scripts/build_intro.py` generates the original light/dark GIF subtitles, PNG stills and SVG tool labels. It requires Pillow. The default font is Segoe UI on Windows; set `PROFILE_BODY_FONT` to another installed TrueType font if needed.

The README selects light/dark sources and requests a still for reduced-motion preferences. Rendering support can vary. All essential role, skills and project information is also readable Markdown text. The old photographic assets are removed; the previous version remains in Git history.

## Daily refresh

`.github/workflows/update-game.yml` regenerates the contribution space shooter daily or manually through Actions. It uses the repository's automatic GitHub token and [gh-space-shooter](https://github.com/czl9707/gh-space-shooter). The `no-amend: true` setting makes new commits instead of rewriting earlier ones.

GitHub can delay scheduled runs and can disable schedules after 60 days of repository inactivity. The hosted workflow must be verified after publication.

The space shooter is a GIF rendered from public contribution data. It is an animation, not a playable game. The initial asset is generated from GitHub's public calendar; scheduled runs use the action's authenticated GitHub API access. The reduced-motion PNG is a still image of the initial game and will not refresh automatically.

## Preview

`python scripts/preview.py` creates `preview.html` using markdown-it-py. This approximates GitHub styling; the published GitHub rendering is authoritative. Preview files are excluded from Git.
