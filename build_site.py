# -*- coding: utf-8 -*-
"""Static site builder for Ascend Lettings (Phase 1).
Generates consistent HTML pages sharing header, footer, schema, cookie banner and WhatsApp float.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://www.ascendlettings.co.uk"
PHONE_DISPLAY = "020 3432 4165"
PHONE_TEL = "+442034324165"
WA_NUMBER = "447418354664"
WA_PREFILL = "Hello%20Ascend%20Lettings%2C%20I%20would%20like%20to%20enquire%20about%20your%20letting%20services."
WA_LINK = f"https://wa.me/{WA_NUMBER}?text={WA_PREFILL}"
EMAIL = "info@ascendlettings.co.uk"

# ---------- Inline SVG icons (Feather-style, 24x24) ----------
IC = {
 "trending": '<polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/>',
 "users": '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 "megaphone": '<path d="M3 11l18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
 "clipboard": '<path d="M9 2h6a1 1 0 0 1 1 1v1h1a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h1V3a1 1 0 0 1 1-1z"/><polyline points="9 14 11 16 15 12"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/>',
 "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="8" y1="13" x2="16" y2="13"/><line x1="8" y1="17" x2="14" y2="17"/>',
 "lifebuoy": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/><line x1="4.93" y1="4.93" x2="9.17" y2="9.17"/><line x1="14.83" y1="14.83" x2="19.07" y2="19.07"/><line x1="14.83" y1="9.17" x2="19.07" y2="4.93"/><line x1="4.93" y1="19.07" x2="9.17" y2="14.83"/>',
 "message": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
 "key": '<path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4"/>',
 "award": '<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89L17 22l-5-3-5 3 1.523-9.11"/>',
 "chat": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
 "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/>',
 "mail": '<path d="M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/><polyline points="22,6 12,13 2,6"/>',
 "check": '<polyline points="20 6 9 17 4 12"/>',
 "arrow": '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>',
 "map": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
 "home": '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
}

def icon(name, cls="", size=24):
    return (f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
            f'viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{IC[name]}</svg>')

WA_ICON = ('<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true" width="32" height="32">'
           '<path d="M16 3C9.4 3 4 8.4 4 15c0 2.1.6 4.1 1.6 5.9L4 29l8.3-1.5c1.7.9 3.6 1.4 5.7 1.4 6.6 0 12-5.4 12-12S22.6 3 16 3zm0 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-4.9.9.9-4.8-.2-.4c-1-1.6-1.5-3.4-1.5-5.3 0-5.6 4.6-10.2 10.2-10.2S26.2 9.4 26.2 15 21.6 24.8 16 24.8zm5.6-7.6c-.3-.2-1.8-.9-2.1-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1c-.3-.2-1.3-.5-2.5-1.5-.9-.8-1.5-1.8-1.7-2.1s0-.5.1-.7l.5-.6c.2-.2.2-.3.3-.6s.1-.4 0-.6l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4s-1.1 1.1-1.1 2.7 1.2 3.1 1.3 3.3c.2.2 2.3 3.6 5.6 5 .8.3 1.4.5 1.9.7.8.2 1.5.2 2.1.1.6-.1 1.8-.7 2.1-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>')

# ---------- Shared components ----------
def head(title, desc, canonical_file, og_type="website", extra_schema=""):
    org_schema = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "RealEstateAgent",
  "name": "Ascend Lettings",
  "description": "Professional UK letting agency helping landlords find quality tenants and tenants find their next home.",
  "url": "{SITE}/",
  "logo": "{SITE}/brand/logo/ascend-lettings-logo-primary.svg",
  "image": "{SITE}/brand/open-graph/og-image.png",
  "telephone": "{PHONE_DISPLAY}",
  "email": "{EMAIL}",
  "areaServed": {{ "@type": "Country", "name": "United Kingdom" }},
  "priceRange": "££",
  "sameAs": []
}}
</script>'''
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{SITE}/{canonical_file}">
  <meta name="theme-color" content="#0B1F3A">
  <meta name="robots" content="index, follow">

  <!-- Open Graph -->
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="Ascend Lettings">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{SITE}/{canonical_file}">
  <meta property="og:image" content="{SITE}/brand/open-graph/og-image.png">
  <meta property="og:locale" content="en_GB">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{SITE}/brand/open-graph/og-image.png">

  <!-- Favicons -->
  <link rel="icon" href="brand/favicon/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" sizes="32x32" href="brand/favicon/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="brand/favicon/favicon-16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="brand/favicon/apple-touch-icon.png">

  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

  <link rel="stylesheet" href="assets/css/main.css">
  {org_schema}
  {extra_schema}
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
'''

def header():
    nav_items = [
        ("index.html", "Home"),
        ("about.html", "About"),
        ("landlords.html", "Landlords"),
        ("tenants.html", "Tenants"),
        ("faqs.html", "FAQs"),
        ("contact.html", "Contact"),
    ]
    nav_html = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in nav_items)
    return f'''  <header class="site-header" id="site-header">
    <div class="header-inner">
      <a class="brand-logo" href="index.html" aria-label="Ascend Lettings home">
        <img class="logo-white" src="brand/logo/ascend-lettings-logo-white.svg" alt="Ascend Lettings" width="620" height="150">
        <img class="logo-colour" src="brand/logo/ascend-lettings-logo-primary.svg" alt="Ascend Lettings" width="620" height="150">
      </a>
      <nav class="main-nav" aria-label="Primary navigation">
        <ul>{nav_html}</ul>
      </nav>
      <div class="header-cta">
        <a class="header-phone" href="tel:{PHONE_TEL}">{icon("phone","",18)} {PHONE_DISPLAY}</a>
        <a class="btn btn--primary" href="landlords.html#landlord-form">Get a Free Valuation</a>
      </div>
      <button class="hamburger" aria-label="Open menu" aria-controls="mobile-nav" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
  <div class="nav-overlay"></div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Mobile navigation">
    <ul>{nav_html}</ul>
    <a class="btn btn--primary btn--block" href="landlords.html#landlord-form">Get a Free Valuation</a>
    <a class="btn btn--whatsapp btn--block mt-1" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>
    <a class="btn btn--secondary btn--block mt-1" href="tel:{PHONE_TEL}">{icon("phone","",18)} {PHONE_DISPLAY}</a>
  </nav>
'''

def footer():
    return f'''  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <img class="footer-logo" src="brand/logo/ascend-lettings-logo-white.svg" alt="Ascend Lettings" width="620" height="150">
          <p>Professional property letting made simple. We help landlords find quality tenants and support tenants in finding their next home &mdash; with transparency and clear communication at every step.</p>
          <div class="footer-badges">
            <span class="footer-badge">ICO Registered</span>
            <span class="footer-badge">Property Redress Scheme</span>
          </div>
        </div>
        <div class="footer-col">
          <h5>Company</h5>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="faqs.html">FAQs</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Services</h5>
          <ul>
            <li><a href="landlords.html">For Landlords</a></li>
            <li><a href="tenants.html">For Tenants</a></li>
            <li><a href="landlords.html#landlord-form">Rental Valuation</a></li>
            <li><a href="tenants.html#tenant-form">Register Requirements</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Get in Touch</h5>
          <ul class="footer-contact">
            <li>{icon("phone","",18)}<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
            <li>{icon("mail","",18)}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li>{icon("chat","",18)}<a href="{WA_LINK}" target="_blank" rel="noopener">WhatsApp: +44 7418 354664</a></li>
          </ul>
        </div>
      </div>
      <p class="footer-disclaimer">Ascend Lettings is a letting agency. ICO Registration Number: [ICO REGISTRATION NUMBER]. Property Redress Scheme Membership Number: [PROPERTY REDRESS SCHEME MEMBERSHIP NUMBER]. Rental valuations are provided as a professional estimate and are not a guarantee of achievable rent.</p>
      <div class="footer-bottom">
        <p>&copy; 2026 Ascend Lettings. All rights reserved.</p>
        <div class="legal-links">
          <a href="index.html">Home</a>
          <a href="landlords.html">Landlords</a>
          <a href="tenants.html">Tenants</a>
          <a href="contact.html">Contact</a>
        </div>
      </div>
    </div>
  </footer>
'''

def floats_and_scripts():
    return f'''  <a class="whatsapp-float" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{WA_ICON}</a>

  <div class="cookie-banner" role="dialog" aria-live="polite" aria-label="Cookie consent">
    <h5>We value your privacy</h5>
    <p>We use cookies to improve your browsing experience and analyse site traffic. You can accept or reject non-essential cookies. See how we handle your data in line with UK GDPR.</p>
    <div class="btn-group">
      <button class="btn btn--secondary" data-cookie="reject">Reject</button>
      <button class="btn btn--navy" data-cookie="accept">Accept</button>
    </div>
  </div>

  <script src="assets/js/main.js" defer></script>
</body>
</html>'''

def page(title, desc, canonical, body, extra_schema=""):
    return head(title, desc, canonical, extra_schema=extra_schema) + header() + body + footer() + floats_and_scripts()

def write(name, content):
    with open(os.path.join(BASE, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name)

# Import page bodies
import pages
pages.build(globals())
