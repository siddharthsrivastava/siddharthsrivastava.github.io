# Siddharth Srivastava — personal website

Static research and professional portfolio for [siddharthsrivastava.github.io](https://siddharthsrivastava.github.io/).

## Local preview

From the repository root:

```sh
python3 -m http.server 3120 --bind 127.0.0.1
```

Open <http://127.0.0.1:3120>. No package installation or build step is required. A local preview does not publish the site.

## Editing

- `index.html`: biography with a brief impact summary and dated Scholar metrics, selected publications, projects, and updates.
- `assets/profile.css`: responsive layout, typography, light/dark appearances, and print styles.
- `assets/profile.js`: appearance preference and accessible mobile navigation.
- `assets/research/`: original conceptual SVG diagrams. These are explanatory illustrations, not experimental outputs or figures reproduced from papers.
- `scripts/build-research-diagrams.py`: regenerates those diagrams using Python's standard library.
- `assets/fonts/`: self-hosted IBM Plex Sans and Source Serif 4, with their OFL licenses.
- `conferencescope/`: existing standalone dashboard; maintained separately from the profile.

The page keeps the existing `#about`, `#publications`, and `#news` anchors. Publication links should point to publisher records or author manuscripts; use “Paper PDF” only for a direct PDF link.

## Content checks

See [SOURCES.md](SOURCES.md) for publication and public announcement sources. Confirm current roles and dates with the owner before changing them. Do not add a downloadable CV, personal email address, private documents, private customer information, credentials, or unverified impact figures. Use the LinkedIn link for contact.

Before publishing, preview desktop and mobile layouts, both appearances, keyboard navigation, the publication accordions, and the ConferenceScope route. Verify new links and keep publication metadata aligned with the official record.
