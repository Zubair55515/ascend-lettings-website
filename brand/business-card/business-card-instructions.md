# Ascend Lettings — Business Card Instructions

This folder contains print-ready business card artwork:

- `business-card-front.svg` — navy front with logo, name and title
- `business-card-back.svg` — off-white back with contact details and compliance line

## Dimensions

- **Standard UK/EU business card:** 85mm × 55mm
- **Standard US business card:** 3.5in × 2in
- The artwork is drawn at **1050 × 600px** (a clean, high-resolution ratio) so it scales crisply for print. Ask your printer to fit to the card size and add bleed (see below).

## Customise before printing

1. Open `business-card-front.svg` in a text editor or vector app (Illustrator, Inkscape, Figma, Affinity Designer).
2. Replace:
   - `[Your Name]` → your full name
   - `[Your Title]` → your role (e.g. *Lettings Manager*)
3. (Optional) On the back, once you have them, you can add the actual ICO and Property Redress Scheme numbers.
4. Save.

## Preparing for print

- **Bleed:** Most printers require 3mm bleed on each edge. Because both backgrounds are solid colour, you can simply extend the background rectangle, or ask the printer to add bleed.
- **Format:** Supply the SVG, or export to **PDF** (preferred for print) or high-resolution **PNG (300dpi)**.
  - Export with Inkscape: `File → Save As → PDF`, or via command line:
    ```bash
    inkscape business-card-front.svg --export-type=pdf --export-filename=front.pdf
    inkscape business-card-front.svg --export-type=png --export-dpi=300 --export-filename=front.png
    ```
- **Colours:** The brand colours are Navy `#0B1F3A` and Gold `#C9A84C`. If your printer needs CMYK, provide:
  - Navy → CMYK 81 / 47 / 0 / 77
  - Gold → CMYK 0 / 16 / 62 / 21
- **Fonts:** The design uses Playfair Display and Inter. If your printer does not have these, convert text to outlines/paths before sending (in Inkscape: select text → **Path → Object to Path**).

## Recommended print options

- Card stock: 350–400gsm
- Finish: matte or soft-touch laminate complements the navy/gold palette
- Double-sided (front + back)
