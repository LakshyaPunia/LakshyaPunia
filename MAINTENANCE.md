# Maintaining this profile

The profile appears at `https://github.com/LakshyaPunia` when this repository is published publicly as `LakshyaPunia/LakshyaPunia`.

## Automatic updates

`.github/workflows/refresh-profile.yml` updates public repository activity daily and supports **Actions → Refresh profile → Run workflow**. It uses GitHub's automatic repository token; no personal token or paid image service is needed. Run the workflow after initial publication to verify the hosted job.

The count excludes forks and the profile repository. Languages are distinct primary languages reported by GitHub, not proficiency ratings. Recent pushes are repository timestamps, not a claim about individual authored commits. A failed API request leaves the previous panel intact.

GitHub can delay scheduled runs and may disable scheduled workflows after 60 days of inactivity in public repositories. Re-enable the workflow from Actions if necessary.

## Content and visuals

- Edit the introduction, project text, and toolkit in `README.md`.
- Keep the `ACTIVITY:START` and `ACTIVITY:END` comments; the refresh script owns the content between them.
- `python scripts/update_profile.py` refreshes the panel locally using Python's standard library. `GH_TOKEN` is optional for public unauthenticated requests.
- `python scripts/build_art.py` rebuilds the banner with Pillow. It defaults to Windows Bahnschrift and Segoe UI; `PROFILE_DISPLAY_FONT` and `PROFILE_BODY_FONT` can point to other installed TrueType fonts.
- `python scripts/preview.py` generates a local preview using `markdown-it-py`. The preview is an approximation; GitHub's rendering is authoritative.

The banner's animated GIF has a 6-second loop. Its PNG is the reduced-motion source and is also linked explicitly, since renderer and browser support for media conditions can vary. All meaningful project information remains ordinary accessible Markdown text.

The source photograph and attribution are in `assets/`. Avoid replacing the source with an unlicensed image.
