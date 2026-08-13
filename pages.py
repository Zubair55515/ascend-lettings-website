# -*- coding: utf-8 -*-
"""Page bodies and FAQ data for Ascend Lettings site builder."""
import json

HERO_IMG = "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1920&q=80"
ABOUT_IMG = "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1200&q=80"
LANDLORD_IMG = "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80"
TENANT_IMG = "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=1200&q=80"
INTERIOR_IMG = "https://images.unsplash.com/photo-1493809842364-78817add7ffb?auto=format&fit=crop&w=1200&q=80"
BLOG1 = "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=800&q=80"
BLOG2 = "https://images.unsplash.com/photo-1554995207-c18c203602cb?auto=format&fit=crop&w=800&q=80"
BLOG3 = "https://images.unsplash.com/photo-1568605114967-8130f3a36994?auto=format&fit=crop&w=800&q=80"

# ---------- FAQ content ----------
LANDLORD_FAQS = [
    ("How do you let my property?", "We start with a consultation to understand your property and goals, provide a free rental valuation, prepare professional marketing, manage enquiries and viewings, carry out tenant referencing and Right to Rent checks, and handle the tenancy administration through to move-in. Our focus is on finding you a suitable tenant with clear communication throughout."),
    ("How is my rental valuation calculated?", "Our rental valuation is a professional estimate based on your property's location, size, condition, specification and comparable local rental evidence. It is intended as guidance to help you make an informed decision and is not a guarantee of the rent that will ultimately be achieved."),
    ("What is tenant referencing and why is it important?", "Referencing helps assess a prospective tenant's suitability and typically includes identity, affordability, employment and previous landlord checks. It gives you greater confidence in the tenancy. We coordinate referencing as part of our tenant-find service."),
    ("What are Right to Rent checks?", "Right to Rent is a legal requirement in England to confirm that a tenant has the right to rent property in the UK. We assist with obtaining and verifying the appropriate documentation before a tenancy begins."),
    ("What documents will I need to provide as a landlord?", "Typically you will need proof of ownership, valid safety certificates (such as a Gas Safety Certificate and an Electrical Installation Condition Report where applicable), an Energy Performance Certificate, and details of any deposit protection requirements. We will guide you on what is needed for your specific property."),
    ("How long does it take to let a property?", "Timescales vary depending on the property, its location, condition and the local rental market. Once marketing begins we work efficiently to generate enquiries and arrange viewings, and we keep you updated at every stage."),
    ("What does your service cover, and what does it not cover?", "We provide letting services including rental valuation, marketing, tenant find, referencing, Right to Rent and tenancy administration. We are a letting agency and do not provide full property management services such as ongoing rent collection, maintenance or property inspections."),
    ("How will you keep me informed during the process?", "Transparent communication is central to how we work. We provide clear updates on marketing, enquiries, viewings and progress towards a completed tenancy, and you can reach us by phone, email or WhatsApp."),
]

TENANT_FAQS = [
    ("Do you have properties available to view right now?", "We do not advertise fake or placeholder listings. The best way to find your next home is to register your requirements with us so we can match you to suitable properties as they become available and keep you informed."),
    ("How do I register my requirements?", "Simply complete the registration form on our Tenants page with your preferred location, budget, property type and move-in date. You can also message us on WhatsApp or call us, and we will note your requirements."),
    ("What is the enquiry and application process?", "Once you have registered and identified a suitable property, you make an enquiry, we guide you through the application, referencing and Right to Rent checks, and then move towards agreeing and setting up the tenancy."),
    ("What documents will I need as a tenant?", "You will typically need photographic identification, proof of address, proof of income or employment, and documentation to support Right to Rent checks. We will let you know exactly what is required for your application."),
    ("What is tenant referencing?", "Referencing is a standard part of renting and usually includes identity, affordability, employment and previous landlord or letting agent checks. It helps confirm that a tenancy is suitable for both you and the landlord."),
    ("What are Right to Rent checks?", "Right to Rent checks confirm that you have the legal right to rent a property in England. We will guide you on the acceptable documents and assist you through the process."),
    ("Are there any fees I should be aware of?", "Tenant fees are regulated in the UK. We will always be transparent about any permitted payments that may apply to your tenancy before you commit to anything."),
    ("How will you keep me updated?", "After you register, we keep in touch as suitable properties arise and guide you through each step of the process. You can reach us by phone, email or WhatsApp at any time."),
]

def faq_item(q, a):
    return f'''<div class="faq-item">
  <button class="faq-question" aria-expanded="false">
    <span>{q}</span>
    <svg class="faq-icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>
  </button>
  <div class="faq-answer"><div class="faq-answer-inner">{a}</div></div>
</div>'''

def faq_schema(faqs):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs
        ]
    }
    return '<script type="application/ld+json">\n' + json.dumps(data, indent=2) + '\n</script>'


def build(g):
    icon = g["icon"]; page = g["page"]; write = g["write"]
    SITE = g["SITE"]; PHONE_DISPLAY = g["PHONE_DISPLAY"]; PHONE_TEL = g["PHONE_TEL"]
    WA_LINK = g["WA_LINK"]; EMAIL = g["EMAIL"]

    def service_card(ic, title, text):
        return f'''<div class="card feature-card reveal">
      <div class="card-icon">{icon(ic)}</div>
      <h4>{title}</h4>
      <p>{text}</p>
    </div>'''

    def step_card(n, title, text):
        return f'''<div class="step-card reveal">
      <span class="step-num">{n}</span>
      <h4>{title}</h4>
      <p>{text}</p>
    </div>'''

    LANDLORD_SERVICES = [
        ("trending", "Rental Valuation", "A free, professional estimate of your property's rental potential based on local market evidence."),
        ("users", "Tenant Find", "We source and introduce suitable prospective tenants for your property."),
        ("megaphone", "Property Marketing", "Professional presentation and marketing to reach the right audience of renters."),
        ("clipboard", "Tenant Referencing", "Identity, affordability and background checks to give you confidence in your tenant."),
        ("shield", "Right to Rent", "Assistance verifying that tenants have the legal right to rent in the UK."),
        ("file", "Tenancy Administration", "Preparation and administration of the paperwork required to set up the tenancy."),
        ("lifebuoy", "Landlord Support", "Clear, knowledgeable support and guidance throughout the letting process."),
        ("message", "Enquiry Management", "We handle enquiries and viewing arrangements so you don't have to."),
        ("key", "Property Letting", "An end-to-end letting service that takes your property from valuation to move-in."),
    ]

    # ============ INDEX ============
    home_faqs = LANDLORD_FAQS[:3] + TENANT_FAQS[:3]
    landlord_intro_cards = "".join(service_card(i, t, d) for i, t, d in LANDLORD_SERVICES[:6])
    how_steps = [
        ("Consultation", "We discuss your property, your goals and the local market."),
        ("Valuation", "We provide a free, professional rental valuation."),
        ("Marketing", "We present and market your property to reach suitable tenants."),
        ("Enquiries", "We manage enquiries and arrange viewings on your behalf."),
        ("Referencing", "We carry out tenant referencing checks."),
        ("Tenancy Admin", "We prepare and administer the tenancy paperwork."),
        ("Move In", "Your tenant moves in and the tenancy begins."),
    ]
    steps_html = "".join(step_card(i+1, t, d) for i, (t, d) in enumerate(how_steps))
    features = [
        ("award", "Professional Service", "A considered, professional approach to letting your property, from valuation to move-in."),
        ("chat", "Transparent Communication", "Clear, honest updates at every stage so you always know where things stand."),
        ("shield", "Compliance-Focused", "We take referencing and Right to Rent seriously to help keep your tenancy compliant."),
        ("lifebuoy", "Dedicated Support", "Approachable support by phone, email and WhatsApp whenever you need us."),
    ]
    features_html = "".join(service_card(i, t, d) for i, t, d in features)
    home_faq_html = "".join(faq_item(q, a) for q, a in home_faqs)
    blog_cards = f'''<article class="blog-card reveal">
      <div class="blog-card-img"><img src="{BLOG1}" alt="A bright, well-presented rental living room" loading="lazy"></div>
      <div class="blog-card-body">
        <span class="tag">Landlords</span>
        <h4>Preparing Your Property to Let: A Practical Checklist</h4>
        <p>Simple, practical steps to help present your property well and attract suitable tenants.</p>
        <a class="read-more" href="faqs.html">Read more {icon("arrow","",16)}</a>
      </div>
    </article>
    <article class="blog-card reveal delay-1">
      <div class="blog-card-img"><img src="{BLOG2}" alt="A person reviewing rental paperwork" loading="lazy"></div>
      <div class="blog-card-body">
        <span class="tag">Guidance</span>
        <h4>Understanding Tenant Referencing and Right to Rent</h4>
        <p>What these checks involve and why they matter for a smooth, compliant tenancy.</p>
        <a class="read-more" href="faqs.html">Read more {icon("arrow","",16)}</a>
      </div>
    </article>
    <article class="blog-card reveal delay-2">
      <div class="blog-card-img"><img src="{BLOG3}" alt="A modern apartment building exterior" loading="lazy"></div>
      <div class="blog-card-body">
        <span class="tag">Tenants</span>
        <h4>How to Register Your Rental Requirements With Us</h4>
        <p>A quick guide to registering so we can match you with suitable homes as they arise.</p>
        <a class="read-more" href="tenants.html">Read more {icon("arrow","",16)}</a>
      </div>
    </article>'''

    index_body = f'''  <main id="main">
    <section class="hero" style="background-image:url('{HERO_IMG}')">
      <div class="container">
        <div class="hero-content">
          <p class="eyebrow" style="color:var(--gold-light)">UK Letting Agency</p>
          <h1>Professional Property Letting Made Simple</h1>
          <p class="hero-sub">We help landlords find quality tenants and tenants find their next home &mdash; with professional service, transparent communication and a compliance-focused approach at every step.</p>
          <div class="btn-group">
            <a class="btn btn--primary btn--lg" href="landlords.html#landlord-form">Get a Free Rental Valuation</a>
            <a class="btn btn--ghost btn--lg" href="landlords.html">Let Your Property With Us</a>
          </div>
          <a class="hero-phone" href="tel:{PHONE_TEL}">{icon("phone","",20)} Call us on {PHONE_DISPLAY}</a>
        </div>
      </div>
    </section>

    <div class="trust-bar">
      <div class="container">
        <ul>
          <li>{icon("shield","",18)} ICO Registered [ICO REGISTRATION NUMBER]</li>
          <li>{icon("check","",18)} Property Redress Scheme Member [PROPERTY REDRESS SCHEME MEMBERSHIP NUMBER]</li>
          <li>{icon("award","",18)} Professional Letting Service</li>
          <li>{icon("chat","",18)} Transparent Communication</li>
        </ul>
      </div>
    </div>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">For Landlords</p>
          <h2 class="section-title">Are You a Landlord?</h2>
          <p class="section-lead">From your first valuation through to move-in, we provide the letting services you need to let your property with confidence.</p>
        </div>
        <div class="grid grid-3">{landlord_intro_cards}</div>
        <div class="text-center mt-2 reveal"><a class="btn btn--navy btn--lg" href="landlords.html">Explore Landlord Services {icon("arrow","",18)}</a></div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">The Process</p>
          <h2 class="section-title">How We Let Your Property</h2>
          <p class="section-lead">A clear, step-by-step approach designed to make letting straightforward.</p>
        </div>
        <div class="grid grid-3 steps">{steps_html}</div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Why Ascend Lettings</p>
          <h2 class="section-title">Why Choose Ascend Lettings</h2>
          <p class="section-lead">A modern letting agency built around professionalism, transparency and compliance.</p>
        </div>
        <div class="grid grid-4">{features_html}</div>
      </div>
    </section>

    <section class="section cta-banner">
      <div class="container">
        <h2>Find Out What Your Property Could Rent For</h2>
        <p>Request a free, no-obligation rental valuation and get a professional estimate of your property's rental potential.</p>
        <div class="btn-group" style="justify-content:center">
          <a class="btn btn--primary btn--lg" href="landlords.html#landlord-form">Get a Free Rental Valuation</a>
          <a class="btn btn--whatsapp btn--lg" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="split">
          <div class="split-media reveal"><img src="{TENANT_IMG}" alt="A couple happily settling into their new rental home"></div>
          <div class="reveal delay-1">
            <p class="eyebrow">For Tenants</p>
            <h2 class="section-title">Looking for Your Next Home?</h2>
            <p>We don't advertise fake or placeholder listings. Instead, register your requirements with us and we'll keep you informed as suitable properties become available.</p>
            <ul class="check-list mt-1">
              <li>{icon("check","",20)} Register your location, budget and property preferences</li>
              <li>{icon("check","",20)} Get guidance through enquiries, applications and referencing</li>
              <li>{icon("check","",20)} Clear support with Right to Rent and the tenancy process</li>
            </ul>
            <div class="btn-group mt-2">
              <a class="btn btn--navy" href="tenants.html#tenant-form">Register Your Requirements</a>
              <a class="btn btn--secondary" href="tenants.html">Tenant Information</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Questions</p>
          <h2 class="section-title">Frequently Asked Questions</h2>
          <p class="section-lead">A few of the questions landlords and tenants ask us most often.</p>
        </div>
        <div class="faq-list">{home_faq_html}</div>
        <div class="text-center mt-2 reveal"><a class="btn btn--secondary" href="faqs.html">View All FAQs {icon("arrow","",18)}</a></div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Insights</p>
          <h2 class="section-title">Latest From Our Blog</h2>
          <p class="section-lead">Practical guidance for landlords and tenants.</p>
        </div>
        <div class="grid grid-3">{blog_cards}</div>
      </div>
    </section>

    <section class="section cta-banner">
      <div class="container">
        <h2>Get in Touch Today</h2>
        <p>Whether you're a landlord ready to let or a tenant searching for your next home, we're here to help. Reach us by phone, email or WhatsApp.</p>
        <div class="btn-group" style="justify-content:center">
          <a class="btn btn--primary btn--lg" href="contact.html">Contact Us</a>
          <a class="btn btn--whatsapp btn--lg" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>
        </div>
      </div>
    </section>
  </main>
'''
    write("index.html", page(
        "Ascend Lettings | Professional Property Letting Made Simple",
        "Ascend Lettings is a professional UK letting agency helping landlords find quality tenants and tenants find their next home. Get a free rental valuation today.",
        "index.html", index_body, extra_schema=faq_schema(home_faqs)))

    # ============ ABOUT ============
    pillars = [
        ("chat", "Transparency", "We communicate openly and honestly, so landlords and tenants always understand each step of the process."),
        ("award", "Professionalism", "We take a considered, professional approach to letting, treating every property and every client with care."),
        ("shield", "Compliance", "We focus on referencing, Right to Rent and correct tenancy administration to support compliant lettings."),
    ]
    pillars_html = "".join(f'''<div class="pillar card reveal">
      <div class="card-icon">{icon(i)}</div>
      <h4>{t}</h4><p>{d}</p></div>''' for i, t, d in pillars)
    about_body = f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / About</p>
        <h1>About Ascend Lettings</h1>
        <p>A modern UK letting agency built around professionalism, transparency and a compliance-focused approach.</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="split">
          <div class="split-media reveal"><img src="{ABOUT_IMG}" alt="A professionally presented residential property"></div>
          <div class="reveal delay-1">
            <p class="eyebrow">Who We Are</p>
            <h2 class="section-title">A Professional, Transparent Letting Agency</h2>
            <p>Ascend Lettings is a letting agency focused on doing the essentials well. We help landlords let their properties and support tenants in finding their next home, combining a professional service with clear, straightforward communication.</p>
            <p>Our approach brings together sensible use of technology, careful attention to compliance, and genuine support for both landlords and tenants. We are ICO registered [ICO REGISTRATION NUMBER] and a member of the Property Redress Scheme [PROPERTY REDRESS SCHEME MEMBERSHIP NUMBER].</p>
            <p>As a letting agency, we concentrate on valuation, marketing, tenant find, referencing, Right to Rent and tenancy administration &mdash; getting your property from valuation to a completed tenancy.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Our Approach</p>
          <h2 class="section-title">Three Pillars That Guide Us</h2>
        </div>
        <div class="grid grid-3">{pillars_html}</div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">What We Believe</p>
          <h2 class="section-title">Our Values</h2>
          <p class="section-lead">The principles behind the way we work with landlords and tenants.</p>
        </div>
        <div class="grid grid-2">
          <div class="card reveal"><div class="card-icon">{icon("chat")}</div><h4>Clear Communication</h4><p>We keep you informed at every stage and are easy to reach by phone, email or WhatsApp.</p></div>
          <div class="card reveal delay-1"><div class="card-icon">{icon("shield")}</div><h4>Doing Things Properly</h4><p>We take compliance seriously, from referencing to Right to Rent and tenancy administration.</p></div>
          <div class="card reveal"><div class="card-icon">{icon("users")}</div><h4>People First</h4><p>Landlords and tenants are treated with respect, honesty and genuine support.</p></div>
          <div class="card reveal delay-1"><div class="card-icon">{icon("trending")}</div><h4>Room to Grow</h4><p>The name Ascend reflects our belief in progress &mdash; helping you move forward with confidence.</p></div>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="grid grid-2">
          <div class="card reveal">
            <div class="card-icon">{icon("key")}</div>
            <h3>Who We Help: Landlords</h3>
            <p>We support landlords who want a professional, transparent service to let their property. From a free rental valuation through to tenant find, referencing and tenancy administration, we help you let with confidence.</p>
            <a class="btn btn--secondary mt-1" href="landlords.html">Landlord Services {icon("arrow","",16)}</a>
          </div>
          <div class="card reveal delay-1">
            <div class="card-icon">{icon("home")}</div>
            <h3>Who We Help: Tenants</h3>
            <p>We support tenants searching for their next home. Register your requirements and we'll guide you through enquiries, applications, referencing and Right to Rent as suitable properties become available.</p>
            <a class="btn btn--secondary mt-1" href="tenants.html">Tenant Information {icon("arrow","",16)}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section cta-banner">
      <div class="container">
        <h2>Ready to Let Your Property?</h2>
        <p>Request a free, no-obligation rental valuation and see how we can help.</p>
        <div class="btn-group" style="justify-content:center">
          <a class="btn btn--primary btn--lg" href="landlords.html#landlord-form">Get a Free Rental Valuation</a>
          <a class="btn btn--whatsapp btn--lg" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>
        </div>
      </div>
    </section>
  </main>
'''
    write("about.html", page(
        "About Us | Ascend Lettings",
        "Learn about Ascend Lettings, a professional UK letting agency focused on transparency, professionalism and compliance for landlords and tenants.",
        "about.html", about_body))

    # ============ LANDLORDS ============
    all_services = "".join(service_card(i, t, d) for i, t, d in LANDLORD_SERVICES)
    land_steps = [
        ("Consultation", "We learn about your property and your goals."),
        ("Free Valuation", "We provide a professional rental valuation."),
        ("Marketing", "We present and market your property to suitable tenants."),
        ("Viewings & Enquiries", "We manage enquiries and arrange viewings."),
        ("Referencing & Right to Rent", "We carry out the appropriate checks."),
        ("Tenancy & Move In", "We administer the tenancy through to move-in."),
    ]
    land_steps_html = "".join(step_card(i+1, t, d) for i, (t, d) in enumerate(land_steps))

    def opt(v):
        return f'<option value="{v}">{v}</option>'
    property_types = ["Flat / Apartment", "Terraced House", "Semi-Detached House", "Detached House", "Studio", "Maisonette", "Bungalow", "Other"]
    services_req = ["Property Letting", "Tenant Find", "Rental Valuation", "Property Marketing", "General Enquiry"]
    status_opts = ["Currently Vacant", "Currently Tenanted", "Owner Occupied", "New Purchase", "Other"]

    landlord_form = f'''<form class="form-card" data-validate id="landlord-form-el">
      <div class="form-success">Thank you &mdash; your enquiry has been received. A member of the Ascend Lettings team will be in touch shortly.</div>
      <div class="form-grid">
        <div class="form-group"><label>Full Name <span class="req">*</span></label><input class="form-control" type="text" name="name" required><span class="field-error">Please enter your full name.</span></div>
        <div class="form-group"><label>Email Address <span class="req">*</span></label><input class="form-control" type="email" name="email" required><span class="field-error">Please enter a valid email address.</span></div>
        <div class="form-group"><label>Phone Number <span class="req">*</span></label><input class="form-control" type="tel" name="phone" required><span class="field-error">Please enter a valid phone number.</span></div>
        <div class="form-group"><label>Property Address <span class="req">*</span></label><input class="form-control" type="text" name="address" required><span class="field-error">Please enter the property address.</span></div>
        <div class="form-group"><label>Property Type <span class="req">*</span></label><select class="form-control" name="property_type" required><option value="">Please select&hellip;</option>{"".join(opt(x) for x in property_types)}</select><span class="field-error">Please select a property type.</span></div>
        <div class="form-group"><label>Service Required <span class="req">*</span></label><select class="form-control" name="service" required><option value="">Please select&hellip;</option>{"".join(opt(x) for x in services_req)}</select><span class="field-error">Please select a service.</span></div>
        <div class="form-group"><label>Bedrooms</label><select class="form-control" name="bedrooms"><option value="">Please select&hellip;</option>{"".join(opt(str(x)) for x in ["Studio","1","2","3","4","5+"])}</select></div>
        <div class="form-group"><label>Bathrooms</label><select class="form-control" name="bathrooms"><option value="">Please select&hellip;</option>{"".join(opt(str(x)) for x in ["1","2","3","4+"])}</select></div>
        <div class="form-group"><label>Furnished / Unfurnished</label><select class="form-control" name="furnished"><option value="">Please select&hellip;</option>{"".join(opt(x) for x in ["Furnished","Unfurnished","Part-Furnished"])}</select></div>
        <div class="form-group"><label>Current Property Status</label><select class="form-control" name="status"><option value="">Please select&hellip;</option>{"".join(opt(x) for x in status_opts)}</select></div>
        <div class="form-group full"><label>Expected Monthly Rent (&pound;)</label><input class="form-control" type="text" name="rent" placeholder="e.g. 1,500 pcm"></div>
        <div class="form-group full"><label>Message</label><textarea class="form-control" name="message" placeholder="Tell us a little about your property and what you need."></textarea></div>
      </div>
      <p class="form-note mt-1">By submitting this form you agree to be contacted by Ascend Lettings regarding your enquiry. We handle your information in line with UK GDPR.</p>
      <button class="btn btn--primary btn--lg btn--block mt-2" type="submit">Get a Free Rental Valuation</button>
    </form>'''

    landlords_body = f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / Landlords</p>
        <h1>Let Your Property With Confidence</h1>
        <p>A professional, transparent letting service &mdash; from a free rental valuation through to a completed tenancy and move-in.</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">What We Offer</p>
          <h2 class="section-title">Landlord Services</h2>
          <p class="section-lead">Everything you need to let your property, delivered with professionalism and clear communication.</p>
        </div>
        <div class="grid grid-3">{all_services}</div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">The Process</p>
          <h2 class="section-title">How It Works</h2>
          <p class="section-lead">A clear, step-by-step letting process.</p>
        </div>
        <div class="grid grid-3 steps">{land_steps_html}</div>
      </div>
    </section>

    <section class="section section--white" id="landlord-form">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Get Started</p>
          <h2 class="section-title">Request Your Free Rental Valuation</h2>
          <p class="section-lead">Complete the form below and we'll be in touch to discuss letting your property.</p>
        </div>
        <div style="max-width:860px;margin:0 auto" class="reveal">{landlord_form}</div>
        <div class="btn-group mt-2" style="justify-content:center">
          <a class="btn btn--navy" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>
          <a class="btn btn--secondary" href="tel:{PHONE_TEL}">{icon("phone","",18)} Request a Callback</a>
        </div>
      </div>
    </section>

    <section class="section cta-banner">
      <div class="container">
        <h2>Let Your Property With Us</h2>
        <p>Speak to Ascend Lettings today and take the first step towards a successful letting.</p>
        <div class="btn-group" style="justify-content:center">
          <a class="btn btn--primary btn--lg" href="#landlord-form">Get a Free Rental Valuation</a>
          <a class="btn btn--whatsapp btn--lg" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>
        </div>
      </div>
    </section>
  </main>
'''
    write("landlords.html", page(
        "Landlords | Let Your Property With Ascend Lettings",
        "Let your property with confidence. Ascend Lettings offers rental valuation, tenant find, marketing, referencing, Right to Rent and tenancy administration for UK landlords.",
        "landlords.html", landlords_body))

    # ============ TENANTS ============
    tenant_steps = [
        ("Register", "Tell us your location, budget and property preferences."),
        ("Enquiry", "Make an enquiry on a suitable property as it becomes available."),
        ("Application", "We guide you through the application process."),
        ("Referencing", "Complete referencing checks with our support."),
        ("Right to Rent", "We help verify your right to rent in the UK."),
        ("Move In", "Agree the tenancy and move into your new home."),
    ]
    tenant_steps_html = "".join(step_card(i+1, t, d) for i, (t, d) in enumerate(tenant_steps))
    tenant_form = f'''<form class="form-card" data-validate id="tenant-form-el">
      <div class="form-success">Thank you &mdash; your requirements have been registered. We'll be in touch as suitable properties become available.</div>
      <div class="form-grid">
        <div class="form-group"><label>Full Name <span class="req">*</span></label><input class="form-control" type="text" name="name" required><span class="field-error">Please enter your full name.</span></div>
        <div class="form-group"><label>Email Address <span class="req">*</span></label><input class="form-control" type="email" name="email" required><span class="field-error">Please enter a valid email address.</span></div>
        <div class="form-group"><label>Phone Number <span class="req">*</span></label><input class="form-control" type="tel" name="phone" required><span class="field-error">Please enter a valid phone number.</span></div>
        <div class="form-group"><label>Preferred Location <span class="req">*</span></label><input class="form-control" type="text" name="location" placeholder="e.g. area or postcode" required><span class="field-error">Please enter a preferred location.</span></div>
        <div class="form-group"><label>Property Type</label><select class="form-control" name="property_type"><option value="">Please select&hellip;</option>{"".join(opt(x) for x in property_types)}</select></div>
        <div class="form-group"><label>Bedrooms</label><select class="form-control" name="bedrooms"><option value="">Please select&hellip;</option>{"".join(opt(str(x)) for x in ["Studio","1","2","3","4","5+"])}</select></div>
        <div class="form-group"><label>Maximum Monthly Rent (&pound;)</label><input class="form-control" type="text" name="max_rent" placeholder="e.g. 1,400 pcm"></div>
        <div class="form-group"><label>Move-in Date</label><input class="form-control" type="date" name="move_in"></div>
        <div class="form-group full"><label>Furnished / Unfurnished</label><select class="form-control" name="furnished"><option value="">Please select&hellip;</option>{"".join(opt(x) for x in ["Furnished","Unfurnished","Part-Furnished","No Preference"])}</select></div>
        <div class="form-group full"><label>Message</label><textarea class="form-control" name="message" placeholder="Tell us more about what you're looking for."></textarea></div>
      </div>
      <p class="form-note mt-1">By submitting this form you agree to be contacted by Ascend Lettings regarding your requirements. We handle your information in line with UK GDPR.</p>
      <button class="btn btn--primary btn--lg btn--block mt-2" type="submit">Register Your Requirements</button>
    </form>'''
    tenants_body = f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / Tenants</p>
        <h1>Find Your Next Rental Property</h1>
        <p>Register your requirements with us and we'll help you find and secure your next home.</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="split">
          <div class="reveal">
            <p class="eyebrow">Honest &amp; Straightforward</p>
            <h2 class="section-title">Looking for Your Next Home?</h2>
            <p>We don't publish fake or placeholder listings. The most effective way to find your next rental is to register your requirements so we can match you to suitable properties as they become available and keep you informed.</p>
            <p>Once you've registered, we'll support you through enquiries, applications, referencing and Right to Rent, all the way to moving in.</p>
            <ul class="check-list mt-1">
              <li>{icon("check","",20)} No fake listings &mdash; just genuine support</li>
              <li>{icon("check","",20)} Guidance at every step of the process</li>
              <li>{icon("check","",20)} Easy to reach by phone, email or WhatsApp</li>
            </ul>
          </div>
          <div class="split-media reveal delay-1"><img src="{INTERIOR_IMG}" alt="A bright, modern rental interior"></div>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">The Process</p>
          <h2 class="section-title">How Renting With Us Works</h2>
        </div>
        <div class="grid grid-3 steps">{tenant_steps_html}</div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Good to Know</p>
          <h2 class="section-title">Tenant Guidance</h2>
          <p class="section-lead">A little preparation makes the process smoother.</p>
        </div>
        <div class="grid grid-3">
          <div class="card reveal"><div class="card-icon">{icon("file")}</div><h4>Documents You May Need</h4><p>Photographic ID, proof of address, and proof of income or employment are commonly required for an application.</p></div>
          <div class="card reveal delay-1"><div class="card-icon">{icon("clipboard")}</div><h4>Referencing</h4><p>Referencing usually covers identity, affordability, employment and previous landlord checks. We'll guide you through it.</p></div>
          <div class="card reveal delay-2"><div class="card-icon">{icon("shield")}</div><h4>Right to Rent</h4><p>You'll need to demonstrate your right to rent in the UK. We'll let you know which documents are acceptable.</p></div>
        </div>
      </div>
    </section>

    <section class="section section--light" id="tenant-form">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Get Started</p>
          <h2 class="section-title">Register Your Requirements</h2>
          <p class="section-lead">Tell us what you're looking for and we'll be in touch as suitable properties arise.</p>
        </div>
        <div style="max-width:860px;margin:0 auto" class="reveal">{tenant_form}</div>
        <div class="btn-group mt-2" style="justify-content:center">
          <a class="btn btn--navy" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>
        </div>
      </div>
    </section>
  </main>
'''
    write("tenants.html", page(
        "Tenants | Find Your Next Rental With Ascend Lettings",
        "Register your rental requirements with Ascend Lettings. We guide tenants through enquiries, applications, referencing and Right to Rent to help you find your next home.",
        "tenants.html", tenants_body))

    # ============ FAQS ============
    land_faq_html = "".join(faq_item(q, a) for q, a in LANDLORD_FAQS)
    ten_faq_html = "".join(faq_item(q, a) for q, a in TENANT_FAQS)
    faqs_body = f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / FAQs</p>
        <h1>Frequently Asked Questions</h1>
        <p>Answers to common questions from landlords and tenants. Can't find what you need? Get in touch.</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">For Landlords</p>
          <h2 class="section-title">Landlord FAQs</h2>
        </div>
        <div class="faq-list">{land_faq_html}</div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">For Tenants</p>
          <h2 class="section-title">Tenant FAQs</h2>
        </div>
        <div class="faq-list">{ten_faq_html}</div>
      </div>
    </section>

    <section class="section cta-banner">
      <div class="container">
        <h2>Still Have Questions?</h2>
        <p>We're happy to help. Reach out and a member of our team will get back to you.</p>
        <div class="btn-group" style="justify-content:center">
          <a class="btn btn--primary btn--lg" href="contact.html">Contact Us</a>
          <a class="btn btn--whatsapp btn--lg" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>
        </div>
      </div>
    </section>
  </main>
'''
    write("faqs.html", page(
        "FAQs | Ascend Lettings",
        "Frequently asked questions for landlords and tenants about letting, rental valuations, referencing, Right to Rent, documents and the tenancy process.",
        "faqs.html", faqs_body, extra_schema=faq_schema(LANDLORD_FAQS + TENANT_FAQS)))

    # ============ CONTACT ============
    subjects = ["Landlord Enquiry", "Tenant Enquiry", "Rental Valuation", "General Enquiry"]
    contact_form = f'''<form class="form-card" data-validate id="contact-form-el">
      <div class="form-success">Thank you for getting in touch. A member of the Ascend Lettings team will respond as soon as possible.</div>
      <div class="form-grid">
        <div class="form-group"><label>Full Name <span class="req">*</span></label><input class="form-control" type="text" name="name" required><span class="field-error">Please enter your full name.</span></div>
        <div class="form-group"><label>Email Address <span class="req">*</span></label><input class="form-control" type="email" name="email" required><span class="field-error">Please enter a valid email address.</span></div>
        <div class="form-group"><label>Phone Number <span class="req">*</span></label><input class="form-control" type="tel" name="phone" required><span class="field-error">Please enter a valid phone number.</span></div>
        <div class="form-group"><label>Subject <span class="req">*</span></label><select class="form-control" name="subject" required><option value="">Please select&hellip;</option>{"".join(opt(x) for x in subjects)}</select><span class="field-error">Please select a subject.</span></div>
        <div class="form-group full"><label>Message <span class="req">*</span></label><textarea class="form-control" name="message" required placeholder="How can we help?"></textarea><span class="field-error">Please enter a message.</span></div>
      </div>
      <p class="form-note mt-1">By submitting this form you agree to be contacted by Ascend Lettings regarding your enquiry. We handle your information in line with UK GDPR.</p>
      <button class="btn btn--primary btn--lg btn--block mt-2" type="submit">Send Message</button>
    </form>'''
    contact_body = f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / Contact</p>
        <h1>Get In Touch</h1>
        <p>Whether you're a landlord or a tenant, we're here to help. Reach us by phone, email or WhatsApp.</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="grid grid-3">
          <div class="contact-card reveal">
            <div class="card-icon">{icon("phone")}</div>
            <h4>Call Us</h4>
            <p>Speak to our team directly.</p>
            <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
          </div>
          <div class="contact-card reveal delay-1">
            <div class="card-icon">{icon("mail")}</div>
            <h4>Email Us</h4>
            <p>We'll get back to you promptly.</p>
            <a href="mailto:{EMAIL}">{EMAIL}</a>
          </div>
          <div class="contact-card reveal delay-2">
            <div class="card-icon">{icon("chat")}</div>
            <h4>WhatsApp</h4>
            <p>Message us for a quick response.</p>
            <a href="{WA_LINK}" target="_blank" rel="noopener">+44 7418 354664</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Send a Message</p>
          <h2 class="section-title">Contact Form</h2>
          <p class="section-lead">Complete the form and we'll be in touch as soon as possible.</p>
        </div>
        <div style="max-width:820px;margin:0 auto" class="reveal">{contact_form}</div>
        <p class="text-center form-note mt-2" style="max-width:720px;margin-left:auto;margin-right:auto">Ascend Lettings is ICO registered [ICO REGISTRATION NUMBER] and a member of the Property Redress Scheme [PROPERTY REDRESS SCHEME MEMBERSHIP NUMBER]. We handle your personal information in line with UK GDPR.</p>
      </div>
    </section>
  </main>
'''
    write("contact.html", page(
        "Contact Us | Ascend Lettings",
        "Contact Ascend Lettings by phone, email or WhatsApp. We're here to help landlords and tenants with letting, valuations and enquiries.",
        "contact.html", contact_body))

    # ============ 404 ============
    body_404 = f'''  <main id="main" class="error-page">
    <div>
      <img src="brand/logo/ascend-lettings-logo-white.svg" alt="Ascend Lettings">
      <div class="code">404</div>
      <h1>Page Not Found</h1>
      <p>Sorry, the page you were looking for could not be found. It may have been moved or no longer exists.</p>
      <div class="btn-group" style="justify-content:center">
        <a class="btn btn--primary" href="index.html">Back to Home</a>
        <a class="btn btn--ghost" href="landlords.html">Landlords</a>
        <a class="btn btn--ghost" href="tenants.html">Tenants</a>
        <a class="btn btn--ghost" href="contact.html">Contact</a>
      </div>
    </div>
  </main>
'''
    # 404 uses a minimal shell (no floats needed but keep for consistency)
    write("404.html", page(
        "Page Not Found | Ascend Lettings",
        "The page you were looking for could not be found. Return to the Ascend Lettings homepage.",
        "404.html", body_404))
