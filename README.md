# Ascend Lettings Website

A professional, static marketing website for **Ascend Lettings** — a UK letting agency. Built as fast, hand-crafted HTML/CSS/JS with a small Python static-site builder, plus a complete brand asset kit (logo, favicons, social media templates, email signature, business card, letterhead and brand guidelines).

- **Live domain:** https://www.ascendlettings.co.uk
- **Email:** info@ascendlettings.co.uk
- **Phone:** 020 3432 4165
- **WhatsApp:** +44 7418 354664

> Ascend Lettings is a **letting agency** (tenant find, referencing, letting set-up). It does **not** provide property management services, and the site must never imply otherwise.

---

## File Structure

```
ascend-lettings-website/
├── index.html                     Homepage
├── about.html                     About us
├── landlords.html                 For landlords
├── tenants.html                   For tenants
├── services.html                  Services overview
├── property-letting.html          Service: property letting
├── tenant-find.html               Service: tenant find
├── property-marketing.html        Service: property marketing
├── rental-valuation.html          Service: rental valuation
├── tenant-referencing.html        Service: tenant referencing
├── right-to-rent.html             Service: right to rent checks
├── faqs.html                      Frequently asked questions
├── contact.html                   Contact us
├── privacy-policy.html            Legal: privacy policy
├── cookie-policy.html             Legal: cookie policy
├── terms.html                     Legal: terms & conditions
├── complaints.html                Legal: complaints procedure
├── 404.html                       Branded error page
├── blog.html                      Blog index (with category filters)
├── blog/                          10 blog articles
│   ├── how-to-rent-out-your-property-uk.html
│   ├── first-time-landlord-guide.html
│   ├── step-by-step-guide-letting-property.html
│   ├── what-landlords-should-know-before-letting.html
│   ├── how-to-choose-a-letting-agent.html
│   ├── letting-agent-vs-letting-yourself.html
│   ├── how-tenant-referencing-works.html
│   ├── what-is-a-rental-valuation.html
│   ├── documents-tenant-needs-uk.html
│   └── how-to-prepare-property-for-tenants.html
│
├── assets/
│   ├── css/main.css               All site styles
│   └── js/main.js                 All site interactivity
│
├── brand/                         Brand asset kit (see below)
│   ├── logo/                       7 logo variants (SVG)
│   ├── favicon/                    favicons + app icons
│   ├── open-graph/                 social share image
│   ├── social/                     social media templates
│   ├── email-signature/            HTML email signature + guide
│   ├── business-card/              business card artwork + guide
│   ├── letterhead/                 letterhead (SVG + HTML)
│   └── brand-guidelines/           BRAND-GUIDELINES.md
│
├── robots.txt                     Crawler directives
├── sitemap.xml                    XML sitemap (all pages)
│
├── build_site.py                  Static site builder (regenerates HTML)
├── pages.py                       Phase 1 page content
├── pages_phase2.py                Phase 2 service & legal pages
├── pages_phase3.py                Phase 3 blog content
└── README.md                      This file
```

> The `.py` files and `README.md` are **build/source tooling only** — they are not part of the deployed website (see deployment instructions).

---

## Brand Assets

Everything in `brand/` follows the Ascend Lettings brand — navy, gold and off-white with Playfair Display + Inter.

- **`logo/`** — 7 logo variants: primary, horizontal, stacked, icon/mark, wordmark, black, white/reversed (all SVG).
- **`favicon/`** — `favicon.ico`, PNG favicons (16/32/48), `apple-touch-icon.png`, PWA icons (192/512) and the SVG source.
- **`open-graph/`** — `og-image.png` (1200×630) for social sharing previews.
- **`social/`** — ready-to-use SVG templates:
  - **instagram/** — profile (1080×1080), post template (1080×1080), story template (1080×1920)
  - **facebook/** — profile (1080×1080), cover (1640×856)
  - **linkedin/** — profile (1080×1080), cover (1584×396)
  - **whatsapp/** — profile (1080×1080)
  - **twitter/** — profile (400×400), header (1500×500)
- **`email-signature/`** — `email-signature.html` (email-safe, table-based) plus a set-up guide for Gmail, Outlook and Apple Mail.
- **`business-card/`** — front and back artwork (SVG) plus a print/customise guide.
- **`letterhead/`** — A4 letterhead in both SVG (print) and HTML (digital, print-ready).
- **`brand-guidelines/`** — `BRAND-GUIDELINES.md`, the full brand guide (voice, logo, colour, typography, do's & don'ts).

---

## GoDaddy cPanel Deployment Instructions

1. **Download or clone** this repository to your computer.
2. **Log in to GoDaddy cPanel** (via your GoDaddy hosting dashboard).
3. Open **File Manager**.
4. Navigate to the **`public_html`** folder.
5. **Upload all website files** — the HTML pages, the `assets/` folder, the `blog/` folder and the `brand/` folder. Upload **everything EXCEPT**:
   - `README.md`
   - the `.git/` folder
   - the Python build files (`build_site.py`, `pages.py`, `pages_phase2.py`, `pages_phase3.py`)
   - `.gitignore`
   > Tip: you can upload a ZIP of the site and use File Manager's **Extract** feature, then delete the excluded files.
6. Ensure **`index.html` sits in the root of `public_html`** (not inside a sub-folder).
7. Visit **https://www.ascendlettings.co.uk** to verify the site loads correctly, including the blog and images.

---

## Placeholders to Replace

Before going fully live, replace these placeholders wherever they appear:

| Placeholder | Where | Replace with |
|---|---|---|
| `[ICO REGISTRATION NUMBER]` | Legal pages, letterhead, email signature, business card | Your ICO registration number |
| `[PROPERTY REDRESS SCHEME MEMBERSHIP NUMBER]` / `[PRS NUMBER]` | Legal pages, letterhead, email signature | Your Property Redress Scheme membership number |
| `[Your Name]` | `brand/email-signature/`, `brand/business-card/business-card-front.svg` | Individual's full name |
| `[Your Title]` | `brand/email-signature/`, `brand/business-card/business-card-front.svg` | Individual's job title |

---

## Brand Colours (quick reference)

| Colour | HEX | Role |
|---|---|---|
| Navy | `#0B1F3A` | Primary |
| Gold | `#C9A84C` | Accent |
| Off-White | `#F7F5F2` | Background |
| Charcoal | `#1A202C` | Dark text/sections |
| White | `#FFFFFF` | Reversed text |
| Mid-Grey | `#4A5568` | Secondary body text |

---

## Fonts

- **Playfair Display** — headings and logo support (weights 400, 700)
- **Inter** — body, navigation, forms, small print (weights 300–700)

Both are already loaded from **Google Fonts** in every HTML page — no extra setup needed.

---

## Contact & Support

For anything relating to this website or the brand, contact **info@ascendlettings.co.uk**.

---

## Website Launch Checklist

- [ ] Replace all `[ICO REGISTRATION NUMBER]` placeholders
- [ ] Replace all `[PROPERTY REDRESS SCHEME MEMBERSHIP NUMBER]` / `[PRS NUMBER]` placeholders
- [ ] Personalise the email signature and business card (`[Your Name]`, `[Your Title]`)
- [ ] Confirm all contact details are correct (phone, email, WhatsApp)
- [ ] Upload all files to `public_html` with `index.html` in the root
- [ ] Test every page loads (no broken links or missing images)
- [ ] Test all forms submit / route to the correct inbox
- [ ] Check the site on mobile, tablet and desktop
- [ ] Confirm the cookie banner works and links to the cookie policy
- [ ] Verify the WhatsApp button opens the correct number
- [ ] Confirm HTTPS is enabled and forced (redirect http → https)
- [ ] Have the privacy policy, terms and complaints procedure reviewed by a solicitor

## SEO Launch Checklist

- [ ] Confirm every page has a unique title and meta description
- [ ] Verify canonical URLs point to `https://www.ascendlettings.co.uk`
- [ ] Submit `sitemap.xml` to Google Search Console
- [ ] Confirm `robots.txt` allows crawling of public pages
- [ ] Verify Open Graph / Twitter card previews (test with a sharing debugger)
- [ ] Check structured data (FAQ, BlogPosting, Breadcrumb) with the Rich Results Test
- [ ] Ensure all images have descriptive `alt` text
- [ ] Set up Google Business Profile and align NAP (name, address, phone)
- [ ] Confirm mobile-friendliness (Google Mobile-Friendly Test)
- [ ] Check page speed (Core Web Vitals / PageSpeed Insights)

---

## Legal Notice

The privacy policy, cookie policy, terms & conditions and complaints procedure included in this site are **templates/starting points**. They **should be reviewed by a qualified solicitor** to ensure they are accurate, complete and compliant with current UK law before the website is published.

---

© 2026 Ascend Lettings. All rights reserved.
