# Ascend Lettings — Website

Professional UK letting agency website. **Phase 1**: brand identity, core pages and front-end framework.

## Brand
- **Colours:** Deep navy `#0B1F3A` (primary), champagne gold `#C9A84C` (accent), off-white `#F7F5F2`, slate `#4A5568`, charcoal `#1A202C`
- **Type:** Playfair Display (headings) + Inter (body/UI) via Google Fonts
- **Logo:** Wordmark "Ascend Lettings" + abstract ascending mark (three rising gold bars)

## Structure
```
├── index.html            # Homepage
├── about.html            # About Us
├── landlords.html        # Landlord services + enquiry form
├── tenants.html          # Tenant registration + guidance
├── faqs.html             # Landlord & tenant FAQs (FAQ schema)
├── contact.html          # Contact details + form
├── 404.html              # Branded error page
├── robots.txt
├── sitemap.xml
├── assets/
│   ├── css/main.css      # Global stylesheet (brand system)
│   └── js/main.js        # Header, menu, accordion, validation, cookies, reveal
├── brand/
│   ├── logo/             # SVG logos (primary, white, black, horizontal, stacked, icon, wordmark)
│   ├── favicon/          # Favicons (ico + PNGs 16/32/48/180/192/512)
│   └── open-graph/       # og-image (SVG + PNG, 1200×630)
└── build_site.py, pages.py  # Static page generators (build tooling)
```

## Build
HTML pages are generated for consistency:
```bash
python3 build_site.py
```

## Notes
- Ascend Lettings is a **letting agency** (not a full property management company).
- Regulatory numbers are placeholders: `[ICO REGISTRATION NUMBER]`, `[PROPERTY REDRESS SCHEME MEMBERSHIP NUMBER]`.
- Forms are client-side validated (front-end only in Phase 1; no back-end submission yet).
- Property images use Unsplash URLs at this stage.

© 2026 Ascend Lettings.
