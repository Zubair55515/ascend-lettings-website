# -*- coding: utf-8 -*-
"""Phase 2 page bodies for Ascend Lettings: detailed service pages and legal pages.
Shares the exact same header, footer, cookie banner, WhatsApp float, CSS and JS as Phase 1
via the shared helpers passed in from build_site.py (page/header/footer/floats).
"""
import pages as p

# ---- Imagery (Unsplash, same convention as Phase 1) ----
SERVICES_IMG = "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1200&q=80"
MARKETING_IMG = "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=1200&q=80"
VALUATION_IMG = "https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=1200&q=80"
REFERENCING_IMG = "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=1200&q=80"


def build(g):
    icon = g["icon"]; page = g["page"]; write = g["write"]
    SITE = g["SITE"]; PHONE_DISPLAY = g["PHONE_DISPLAY"]; PHONE_TEL = g["PHONE_TEL"]
    WA_LINK = g["WA_LINK"]; EMAIL = g["EMAIL"]
    faq_item = p.faq_item; faq_schema = p.faq_schema

    # ---------- shared option data ----------
    def opt(v, sel=""):
        s = " selected" if sel == v else ""
        return f'<option value="{v}"{s}>{v}</option>'

    property_types = ["Flat / Apartment", "Terraced House", "Semi-Detached House",
                      "Detached House", "Studio", "Maisonette", "Bungalow", "Other"]
    val_property_types = ["Flat / Apartment", "Terraced House", "Semi-Detached House",
                          "Detached House", "Studio", "HMO Room", "Other"]
    services_req = ["Property Letting", "Tenant Find", "Rental Valuation",
                    "Property Marketing", "General Enquiry"]
    status_opts = ["Currently Vacant", "Currently Tenanted", "Owner Occupied",
                   "New Purchase", "Other"]
    bedrooms = ["Studio", "1", "2", "3", "4", "5+"]
    bathrooms = ["1", "2", "3", "4+"]
    furnished = ["Furnished", "Unfurnished", "Part-Furnished"]

    # ---------- shared components ----------
    def service_card(ic, title, text, href=None):
        link = (f'<a class="read-more mt-1" href="{href}">Learn more {icon("arrow","",16)}</a>'
                if href else "")
        return f'''<div class="card feature-card reveal">
      <div class="card-icon">{icon(ic)}</div>
      <h4>{title}</h4>
      <p>{text}</p>
      {link}
    </div>'''

    def process_step(n, ic, title, paras):
        para_html = "".join(f"<p>{t}</p>" for t in paras)
        return f'''<div class="card reveal process-step">
      <div class="process-step-head">
        <span class="step-num">{n}</span>
        <div class="card-icon">{icon(ic)}</div>
      </div>
      <h3>{title}</h3>
      {para_html}
    </div>'''

    def landlord_form(preselect="", heading="Get a Free Rental Valuation"):
        form_type = f"{preselect} Enquiry" if preselect else "Landlord Enquiry"
        return f'''<form class="form-card" data-validate id="landlord-form-el" action="mail-handler.php" method="POST">
      <div class="form-success">Thank you &mdash; your enquiry has been received. A member of the Ascend Lettings team will be in touch shortly.</div>
      <div class="form-error"></div>
      <input type="hidden" name="form_type" value="{form_type}">
      <div class="hp-field" aria-hidden="true"><label>Leave this field blank</label><input type="text" name="website" tabindex="-1" autocomplete="off"></div>
      <div class="form-grid">
        <div class="form-group"><label>Full Name <span class="req">*</span></label><input class="form-control" type="text" name="name" required><span class="field-error">Please enter your full name.</span></div>
        <div class="form-group"><label>Email Address <span class="req">*</span></label><input class="form-control" type="email" name="email" required><span class="field-error">Please enter a valid email address.</span></div>
        <div class="form-group"><label>Phone Number <span class="req">*</span></label><input class="form-control" type="tel" name="phone" required><span class="field-error">Please enter a valid phone number.</span></div>
        <div class="form-group"><label>Property Address <span class="req">*</span></label><input class="form-control" type="text" name="address" required><span class="field-error">Please enter the property address.</span></div>
        <div class="form-group"><label>Property Type <span class="req">*</span></label><select class="form-control" name="property_type" required><option value="">Please select&hellip;</option>{"".join(opt(x) for x in property_types)}</select><span class="field-error">Please select a property type.</span></div>
        <div class="form-group"><label>Service Required <span class="req">*</span></label><select class="form-control" name="service" required><option value="">Please select&hellip;</option>{"".join(opt(x, preselect) for x in services_req)}</select><span class="field-error">Please select a service.</span></div>
        <div class="form-group"><label>Bedrooms</label><select class="form-control" name="bedrooms"><option value="">Please select&hellip;</option>{"".join(opt(x) for x in bedrooms)}</select></div>
        <div class="form-group"><label>Bathrooms</label><select class="form-control" name="bathrooms"><option value="">Please select&hellip;</option>{"".join(opt(x) for x in bathrooms)}</select></div>
        <div class="form-group"><label>Furnished / Unfurnished</label><select class="form-control" name="furnished"><option value="">Please select&hellip;</option>{"".join(opt(x) for x in furnished)}</select></div>
        <div class="form-group"><label>Current Property Status</label><select class="form-control" name="status"><option value="">Please select&hellip;</option>{"".join(opt(x) for x in status_opts)}</select></div>
        <div class="form-group full"><label>Expected Monthly Rent (&pound;)</label><input class="form-control" type="text" name="rent" placeholder="e.g. 1,500 pcm"></div>
        <div class="form-group full"><label>Message</label><textarea class="form-control" name="message" placeholder="Tell us a little about your property and what you need."></textarea></div>
      </div>
      <p class="form-note mt-1">By submitting this form you agree to be contacted by Ascend Lettings regarding your enquiry. We handle your information in line with UK GDPR.</p>
      <button class="btn btn--primary btn--lg btn--block mt-2" type="submit">{heading}</button>
    </form>'''

    def valuation_form():
        return f'''<form class="form-card" data-validate id="valuation-form-el" action="mail-handler.php" method="POST">
      <div class="form-success">Thank you &mdash; your rental valuation request has been received. A member of the Ascend Lettings team will be in touch shortly.</div>
      <div class="form-error"></div>
      <input type="hidden" name="form_type" value="Rental Valuation Request">
      <div class="hp-field" aria-hidden="true"><label>Leave this field blank</label><input type="text" name="website" tabindex="-1" autocomplete="off"></div>
      <div class="form-grid">
        <div class="form-group"><label>Full Name <span class="req">*</span></label><input class="form-control" type="text" name="name" required><span class="field-error">Please enter your full name.</span></div>
        <div class="form-group"><label>Email Address <span class="req">*</span></label><input class="form-control" type="email" name="email" required><span class="field-error">Please enter a valid email address.</span></div>
        <div class="form-group"><label>Phone Number <span class="req">*</span></label><input class="form-control" type="tel" name="phone" required><span class="field-error">Please enter a valid phone number.</span></div>
        <div class="form-group"><label>Property Address <span class="req">*</span></label><input class="form-control" type="text" name="address" required><span class="field-error">Please enter the property address.</span></div>
        <div class="form-group"><label>Property Type <span class="req">*</span></label><select class="form-control" name="property_type" required><option value="">Please select&hellip;</option>{"".join(opt(x) for x in val_property_types)}</select><span class="field-error">Please select a property type.</span></div>
        <div class="form-group"><label>Current Status</label><select class="form-control" name="status"><option value="">Please select&hellip;</option>{"".join(opt(x) for x in status_opts)}</select></div>
        <div class="form-group"><label>Bedrooms</label><select class="form-control" name="bedrooms"><option value="">Please select&hellip;</option>{"".join(opt(x) for x in bedrooms)}</select></div>
        <div class="form-group"><label>Bathrooms</label><select class="form-control" name="bathrooms"><option value="">Please select&hellip;</option>{"".join(opt(x) for x in bathrooms)}</select></div>
        <div class="form-group full"><label>Furnished / Unfurnished</label><select class="form-control" name="furnished"><option value="">Please select&hellip;</option>{"".join(opt(x) for x in furnished)}</select></div>
        <div class="form-group full"><label>Additional Information</label><textarea class="form-control" name="message" placeholder="Anything else that may help with your valuation (condition, recent works, parking, outside space, etc.)."></textarea></div>
      </div>
      <p class="form-note mt-1">By submitting this form you agree to be contacted by Ascend Lettings regarding your rental valuation. We handle your information in line with UK GDPR. A rental valuation is a professional estimate and not a guarantee of achievable rent.</p>
      <button class="btn btn--primary btn--lg btn--block mt-2" type="submit">Request Your Free Rental Valuation</button>
    </form>'''

    def cta(title, text, primary_label, primary_href, wa=True):
        wa_btn = (f'<a class="btn btn--whatsapp btn--lg" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>'
                  if wa else "")
        return f'''<section class="section cta-banner">
      <div class="container">
        <h2>{title}</h2>
        <p>{text}</p>
        <div class="btn-group" style="justify-content:center">
          <a class="btn btn--primary btn--lg" href="{primary_href}">{primary_label}</a>
          {wa_btn}
        </div>
      </div>
    </section>'''

    # ============================================================
    # SERVICES OVERVIEW
    # ============================================================
    landlord_service_data = [
        ("key", "Property Letting", "An end-to-end letting service that takes your property from valuation right through to move-in.", "property-letting.html"),
        ("users", "Tenant Find", "We source, engage and introduce suitable prospective tenants for your property.", "tenant-find.html"),
        ("megaphone", "Property Marketing", "Professional presentation and marketing to reach the right audience of renters.", "property-marketing.html"),
        ("trending", "Rental Valuation", "A free, professional estimate of your property's rental potential based on local evidence.", "rental-valuation.html"),
        ("clipboard", "Tenant Referencing", "Identity, affordability and background checks to help you let with confidence.", "tenant-referencing.html"),
        ("shield", "Right to Rent", "Assistance verifying that tenants have the legal right to rent in England.", "right-to-rent.html"),
        ("file", "Tenancy Administration", "Preparation and administration of the paperwork required to set up the tenancy.", "property-letting.html"),
    ]
    tenant_service_data = [
        ("search", "Property Enquiries", "Enquire about suitable properties as they become available and get a prompt, helpful response."),
        ("edit", "Register Requirements", "Tell us your location, budget and preferences so we can match you to the right homes."),
        ("lifebuoy", "Application Guidance", "Clear guidance through the application process from enquiry to agreeing a tenancy."),
        ("clipboard", "Referencing Guidance", "Practical help understanding referencing and the documents you may need to provide."),
    ]
    landlord_cards = "".join(service_card(i, t, d, h) for i, t, d, h in landlord_service_data)
    tenant_cards = "".join(service_card(i, t, d) for i, t, d in tenant_service_data)

    services_body = f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / Services</p>
        <h1>Our Letting Services</h1>
        <p>A professional, transparent range of letting services for landlords, and genuine support for tenants searching for their next home.</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">What We Do</p>
          <h2 class="section-title">How We Help Landlords and Tenants</h2>
          <p class="section-lead">Ascend Lettings brings together everything needed to let a property well &mdash; from an initial rental valuation through to marketing, tenant find, referencing, Right to Rent and tenancy administration. For tenants, we offer straightforward guidance and support throughout your search.</p>
        </div>
        <div class="callout reveal">
          <div class="card-icon">{icon("info")}</div>
          <p><strong>We specialise in property letting and tenant finding.</strong> We do not currently offer ongoing property management services such as rent collection, maintenance, repairs or property inspections.</p>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">For Landlords</p>
          <h2 class="section-title">Landlord Services</h2>
          <p class="section-lead">Explore each service in detail, or request a free rental valuation to get started.</p>
        </div>
        <div class="grid grid-3">{landlord_cards}</div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">For Tenants</p>
          <h2 class="section-title">Tenant Services</h2>
          <p class="section-lead">We don't advertise fake listings &mdash; instead we help you register, enquire and progress with confidence.</p>
        </div>
        <div class="grid grid-4">{tenant_cards}</div>
        <div class="text-center mt-2 reveal"><a class="btn btn--navy btn--lg" href="tenants.html">Tenant Information {icon("arrow","",18)}</a></div>
      </div>
    </section>

    {cta("Get a Free Rental Valuation",
         "Find out what your property could rent for with a free, no-obligation professional estimate.",
         "Get a Free Rental Valuation", "rental-valuation.html")}
  </main>
'''
    write("services.html", page(
        "Our Letting Services | Ascend Lettings",
        "Explore Ascend Lettings' letting services for landlords \u2014 property letting, tenant find, marketing, rental valuation, referencing and Right to Rent \u2014 plus support for tenants.",
        "services.html", services_body))


    # ============================================================
    # PROPERTY LETTING
    # ============================================================
    letting_steps = [
        ("clipboard", "Consultation", [
            "Every successful let begins with a proper conversation. We take the time to understand your property, your priorities and your timescales, whether you are letting for the first time or have let before.",
            "We discuss the type of tenant you are hoping to attract, your preferences around furnishing and tenancy length, and any questions you have about the process. This helps us tailor our approach from the outset.",
            "There is no obligation at this stage &mdash; it is simply an opportunity to understand how we can help and for you to decide whether Ascend Lettings is the right fit."]),
        ("trending", "Rental Valuation", [
            "We provide a free, professional rental valuation based on your property's location, size, condition, specification and comparable local rental evidence.",
            "Our valuation is intended as clear guidance to help you make an informed decision. It is a professional estimate and not a guarantee of the rent that will ultimately be achieved.",
            "You can <a href=\"rental-valuation.html\">request a free rental valuation</a> at any time to get started."]),
        ("home", "Preparation", [
            "Well-prepared properties tend to attract stronger interest. We offer practical, honest guidance on presenting your property to appeal to suitable tenants.",
            "We will also talk you through the documents and safety requirements typically needed before a tenancy can begin, such as an Energy Performance Certificate and relevant safety certificates, so there are no surprises later on."]),
        ("megaphone", "Marketing", [
            "Once your property is ready, we prepare professional marketing and present it to reach the right audience of renters across major property portals and our own channels.",
            "Clear descriptions and strong presentation help your property stand out. You can read more about our approach on our <a href=\"property-marketing.html\">property marketing</a> page."]),
        ("message", "Enquiries", [
            "We manage incoming enquiries on your behalf, responding promptly and professionally to prospective tenants.",
            "By handling enquiries for you, we save you time and ensure interested applicants receive the information they need to progress."]),
        ("users", "Viewings & Engagement", [
            "We arrange and coordinate viewings, engaging with prospective tenants to understand their circumstances and suitability for your property.",
            "Throughout this stage we keep you informed of interest and feedback, so you always have a clear picture of how the marketing is progressing."]),
        ("clipboard", "Referencing", [
            "Once a prospective tenant is identified, we coordinate tenant referencing to help assess their suitability. This typically covers identity, affordability, employment and previous landlord checks.",
            "Referencing gives you greater confidence in the tenancy. You can find out more on our <a href=\"tenant-referencing.html\">tenant referencing</a> page."]),
        ("shield", "Right to Rent", [
            "We assist with Right to Rent checks, confirming that a prospective tenant has the legal right to rent property in England before the tenancy begins.",
            "We will help obtain and verify the appropriate documentation. See our <a href=\"right-to-rent.html\">Right to Rent</a> page for general guidance."]),
        ("file", "Tenancy Administration", [
            "We prepare and administer the paperwork required to set up the tenancy, helping to ensure the essentials are correctly in place.",
            "Clear administration at this stage helps the tenancy start on a professional footing for both you and your tenant."]),
        ("key", "Move-In", [
            "With the paperwork complete and checks in place, your tenant moves in and the tenancy begins.",
            "As a letting agency focused on tenant find, our role centres on getting you to a well-organised move-in. We do not provide ongoing property management such as rent collection, maintenance or inspections after move-in."]),
    ]
    letting_steps_html = "".join(process_step(i + 1, ic, t, ps)
                                 for i, (ic, t, ps) in enumerate(letting_steps))

    why_features = [
        ("award", "Professional Service", "A considered, professional approach to letting your property, from valuation right through to move-in."),
        ("chat", "Transparent Communication", "Clear, honest updates at every stage so you always know exactly where things stand."),
        ("shield", "Compliance-Focused", "We take referencing and Right to Rent seriously to help keep your tenancy on the right footing."),
        ("lifebuoy", "Dedicated Support", "Approachable support by phone, email and WhatsApp whenever you need us."),
    ]
    why_html = "".join(service_card(i, t, d) for i, t, d in why_features)

    letting_body = f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / <a href="services.html">Services</a> / Property Letting</p>
        <h1>Property Letting &mdash; From Instruction to Move-In</h1>
        <p>A clear, professional letting service that guides your property through every stage, from your first consultation to your tenant moving in.</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">The Full Process</p>
          <h2 class="section-title">How We Let Your Property</h2>
          <p class="section-lead">Ten clear steps, delivered with professionalism and transparent communication throughout.</p>
        </div>
        <div class="process-list">{letting_steps_html}</div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Why Ascend Lettings</p>
          <h2 class="section-title">Why Choose Ascend Lettings?</h2>
          <p class="section-lead">A modern letting agency built around professionalism, transparency and compliance.</p>
        </div>
        <div class="grid grid-4">{why_html}</div>
      </div>
    </section>

    <section class="section section--white" id="landlord-form">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Get Started</p>
          <h2 class="section-title">Start the Letting Process Today</h2>
          <p class="section-lead">Complete the form below and we'll be in touch to discuss letting your property.</p>
        </div>
        <div style="max-width:860px;margin:0 auto" class="reveal">{landlord_form(preselect="Property Letting", heading="Start the Letting Process")}</div>
        <div class="btn-group mt-2" style="justify-content:center">
          <a class="btn btn--navy" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>
          <a class="btn btn--secondary" href="tel:{PHONE_TEL}">{icon("phone","",18)} Request a Callback</a>
        </div>
      </div>
    </section>

    {cta("Start the Letting Process Today",
         "Take the first step towards a successful let with a professional, transparent service.",
         "Start the Letting Process", "#landlord-form")}
  </main>
'''
    write("property-letting.html", page(
        "Property Letting \u2014 From Instruction to Move-In | Ascend Lettings",
        "Ascend Lettings' full property letting process explained step by step \u2014 consultation, valuation, marketing, referencing, Right to Rent and tenancy administration through to move-in.",
        "property-letting.html", letting_body))

    # ============================================================
    # TENANT FIND
    # ============================================================
    included = [
        "Professional marketing and presentation of your property",
        "Managing applicant enquiries and arranging viewings",
        "Engaging with prospective tenants to assess suitability",
        "Coordinating tenant referencing checks",
        "Assisting with Right to Rent checks",
        "Preparing and administering the tenancy paperwork",
        "Clear communication with you as the landlord throughout",
    ]
    not_included = [
        "Ongoing property management once the tenancy has begun",
        "Rent collection and rent arrears handling",
        "Repairs, maintenance and contractor management",
        "Routine property inspections during the tenancy",
    ]
    included_html = "".join(f'<li>{icon("check","",20)} {t}</li>' for t in included)
    not_included_html = "".join(f'<li>{icon("alert","",20)} {t}</li>' for t in not_included)

    tf_steps = [
        ("Instruction & Valuation", "We agree the details and provide a free rental valuation."),
        ("Marketing", "We prepare and market your property to reach suitable tenants."),
        ("Enquiries & Viewings", "We manage applicant enquiries and arrange viewings."),
        ("Referencing & Right to Rent", "We coordinate referencing and assist with Right to Rent checks."),
        ("Tenancy Administration", "We prepare and administer the tenancy paperwork."),
        ("Move-In", "Your tenant moves in and the tenancy begins."),
    ]
    tf_steps_html = "".join(f'''<div class="step-card reveal"><span class="step-num">{i+1}</span><h4>{t}</h4><p>{d}</p></div>'''
                            for i, (t, d) in enumerate(tf_steps))

    tenant_find_body = f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / <a href="services.html">Services</a> / Tenant Find</p>
        <h1>Our Tenant Find Service</h1>
        <p>A focused, professional service that finds and introduces a suitable tenant for your property &mdash; from marketing right through to move-in.</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="split">
          <div class="reveal">
            <p class="eyebrow">What It Is</p>
            <h2 class="section-title">A Complete Tenant Find Service</h2>
            <p>Our tenant find service covers everything needed to secure a suitable tenant: professional marketing, managing applicant enquiries, coordinating referencing, assisting with Right to Rent, and handling the tenancy administration &mdash; with clear landlord communication at every step.</p>
            <p>We keep you informed throughout, from the first enquiry to the day your tenant moves in, so you always know how your let is progressing.</p>
          </div>
          <div class="callout reveal delay-1">
            <div class="card-icon">{icon("info")}</div>
            <p><strong>This is a tenant-find service, not ongoing property management.</strong> Our role is to find and introduce a suitable tenant and set the tenancy up correctly. We do not provide rent collection, maintenance or inspections once the tenancy is underway.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="grid grid-2">
          <div class="card reveal">
            <h3>What's Included</h3>
            <ul class="check-list mt-1">{included_html}</ul>
          </div>
          <div class="card reveal delay-1">
            <h3>What's Not Included</h3>
            <ul class="check-list check-list--muted mt-1">{not_included_html}</ul>
            <p class="form-note mt-1">We're always upfront about this so you know exactly what to expect from our service.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">The Process</p>
          <h2 class="section-title">Tenant Find Timeline</h2>
          <p class="section-lead">A clear, step-by-step path from instruction to move-in.</p>
        </div>
        <div class="grid grid-3 steps">{tf_steps_html}</div>
      </div>
    </section>

    <section class="section section--light" id="landlord-form">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Get Started</p>
          <h2 class="section-title">Find a Tenant for Your Property</h2>
          <p class="section-lead">Complete the form below and we'll be in touch to discuss finding a tenant.</p>
        </div>
        <div style="max-width:860px;margin:0 auto" class="reveal">{landlord_form(preselect="Tenant Find", heading="Find a Tenant")}</div>
        <div class="btn-group mt-2" style="justify-content:center">
          <a class="btn btn--navy" href="rental-valuation.html">Get a Free Rental Valuation</a>
          <a class="btn btn--secondary" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>
        </div>
      </div>
    </section>

    {cta("Find a Tenant With Confidence",
         "Let us find and introduce a suitable tenant for your property, with transparent communication throughout.",
         "Find a Tenant", "#landlord-form")}
  </main>
'''
    write("tenant-find.html", page(
        "Our Tenant Find Service | Ascend Lettings",
        "Ascend Lettings' tenant find service covers marketing, enquiries, referencing, Right to Rent and tenancy administration \u2014 a tenant-find service, not ongoing property management.",
        "tenant-find.html", tenant_find_body))


    # ============================================================
    # PROPERTY MARKETING
    # ============================================================
    marketing_breakdown = [
        ("camera", "Professional Photography", "Strong, well-lit imagery is central to presenting a property well. We focus on clear, attractive photography that shows your property at its best and helps it stand out to prospective tenants."),
        ("edit", "Compelling Property Descriptions", "We write clear, accurate and engaging property descriptions that highlight the features that matter most to renters, from layout and location to key selling points, always presented honestly."),
        ("megaphone", "Online Marketing", "We market your property online to reach a wide audience of prospective tenants across major property portals and our own channels, giving your property strong visibility."),
        ("message", "Enquiry Management", "We handle incoming enquiries promptly and professionally, providing prospective tenants with the information they need and arranging viewings on your behalf."),
        ("users", "Applicant Communication", "We keep in touch with interested applicants, understand their circumstances and keep you updated on interest and feedback throughout the marketing period."),
        ("award", "Professional Presentation", "From the first impression to the finer details, we present your property professionally and consistently, reflecting well on both your property and you as a landlord."),
    ]
    marketing_cards = "".join(service_card(i, t, d) for i, t, d in marketing_breakdown)

    marketing_body = f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / <a href="services.html">Services</a> / Property Marketing</p>
        <h1>Professional Property Marketing</h1>
        <p>Thoughtful presentation and effective marketing to help your property reach the right audience of renters.</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="split">
          <div class="reveal">
            <p class="eyebrow">Our Approach</p>
            <h2 class="section-title">Marketing That Reaches the Right Tenants</h2>
            <p>How a property is presented and marketed makes a real difference to the interest it attracts. Our approach brings together professional photography, well-written descriptions, online marketing and attentive enquiry management to help your property stand out.</p>
            <p>We market your property across major property portals and our own channels, and we handle applicant communication throughout, so interested renters receive a prompt, professional response.</p>
          </div>
          <div class="split-media reveal delay-1"><img src="{MARKETING_IMG}" alt="A professionally presented, well-lit rental property interior"></div>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">The Detail</p>
          <h2 class="section-title">How We Market Your Property</h2>
          <p class="section-lead">A clear, professional marketing process from presentation to enquiry management.</p>
        </div>
        <div class="grid grid-3">{marketing_cards}</div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="split">
          <div class="callout reveal">
            <div class="card-icon">{icon("camera")}</div>
            <p><strong>Why professional imagery matters.</strong> Most renters begin their search online, where photographs form the crucial first impression. Clear, attractive imagery helps your property attract more interest and present at its best from the very first click.</p>
          </div>
          <div class="reveal delay-1">
            <p class="eyebrow">Enquiry Management</p>
            <h2 class="section-title">Turning Interest Into Viewings</h2>
            <p>Generating enquiries is only part of the picture &mdash; responding to them well is just as important. We manage enquiries promptly, provide prospective tenants with clear information, and arrange viewings on your behalf.</p>
            <p>Throughout the marketing period we keep you informed of interest and feedback, so you always know how your property is performing.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--light" id="landlord-form">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Get Started</p>
          <h2 class="section-title">Request Property Marketing Info</h2>
          <p class="section-lead">Tell us about your property and we'll be in touch to discuss marketing it effectively.</p>
        </div>
        <div style="max-width:860px;margin:0 auto" class="reveal">{landlord_form(preselect="Property Marketing", heading="Request Property Marketing Info")}</div>
        <div class="btn-group mt-2" style="justify-content:center">
          <a class="btn btn--navy" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>
          <a class="btn btn--secondary" href="rental-valuation.html">Get a Free Rental Valuation</a>
        </div>
      </div>
    </section>

    {cta("Present Your Property at Its Best",
         "Speak to us about professional marketing that reaches the right audience of renters.",
         "Request Property Marketing Info", "#landlord-form")}
  </main>
'''
    write("property-marketing.html", page(
        "Professional Property Marketing | Ascend Lettings",
        "Professional property marketing from Ascend Lettings \u2014 photography, compelling descriptions, online marketing across major portals and attentive enquiry management.",
        "property-marketing.html", marketing_body))

    # ============================================================
    # RENTAL VALUATION (with FAQ schema)
    # ============================================================
    factors = [
        ("map", "Location", "Where your property is situated, including the local area, transport links and demand from renters."),
        ("home", "Property Type", "Whether it is a flat, house, studio or room, and how it compares with similar local properties."),
        ("key", "Bedrooms & Size", "The number of bedrooms and bathrooms and the overall size and layout of the property."),
        ("award", "Condition & Specification", "The standard of finish, fixtures and general condition of the property."),
        ("file", "Furnishing", "Whether the property is furnished, part-furnished or unfurnished can influence its appeal."),
        ("trending", "Market Demand", "Current demand in the local rental market and comparable rental evidence."),
    ]
    factors_html = "".join(service_card(i, t, d) for i, t, d in factors)
    expect_steps = [
        ("Request", "Complete the valuation form with your property details."),
        ("Review", "We review your information alongside comparable local rental evidence."),
        ("Valuation", "We provide a professional estimate of your property's rental potential."),
        ("Next Steps", "If you'd like to proceed, we'll talk you through letting your property."),
    ]
    expect_html = "".join(f'''<div class="step-card reveal"><span class="step-num">{i+1}</span><h4>{t}</h4><p>{d}</p></div>'''
                          for i, (t, d) in enumerate(expect_steps))
    benefits = [
        ("info", "Make Informed Decisions", "A professional estimate helps you plan and make informed decisions about letting your property."),
        ("chat", "No Obligation", "Our valuation is free and comes with no obligation to proceed."),
        ("shield", "Grounded in Evidence", "We base our estimate on your property's characteristics and comparable local rental evidence."),
    ]
    benefits_html = "".join(service_card(i, t, d) for i, t, d in benefits)

    VAL_FAQS = [
        ("Is the rental valuation free?", "Yes. Our rental valuation is free and comes with no obligation. It is designed to give you a clear, professional estimate of your property's rental potential."),
        ("Is the valuation a guaranteed rent figure?", "No. A rental valuation is a professional estimate based on your property and comparable local evidence. It is intended as guidance and is not a guarantee of the rent that will ultimately be achieved."),
        ("What information do you need for a valuation?", "It helps to know the property address, type, number of bedrooms and bathrooms, its condition and whether it will be furnished or unfurnished. You can provide these details on our valuation form, along with any additional information."),
        ("How is the rental value determined?", "We consider factors such as location, property type, size, condition, specification, furnishing and current market demand, alongside comparable local rental evidence, to arrive at a professional estimate."),
        ("What happens after I request a valuation?", "A member of our team will be in touch to discuss your property and provide a professional rental estimate. If you'd like to proceed, we can then talk you through the process of letting your property."),
    ]
    val_faq_html = "".join(faq_item(q, a) for q, a in VAL_FAQS)

    valuation_body = f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / <a href="services.html">Services</a> / Rental Valuation</p>
        <h1>Find Out What Your Property Could Rent For</h1>
        <p>Request Your Free Rental Valuation &mdash; a professional estimate of your property's rental potential, with no obligation.</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">What Affects Rental Value</p>
          <h2 class="section-title">What Determines What Your Property Could Rent For</h2>
          <p class="section-lead">Several factors influence a property's rental potential. We consider them together, alongside comparable local evidence.</p>
        </div>
        <div class="grid grid-3">{factors_html}</div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">What to Expect</p>
          <h2 class="section-title">The Valuation Process</h2>
          <p class="section-lead">A simple, transparent process from request to professional estimate.</p>
        </div>
        <div class="grid grid-4 steps">{expect_html}</div>
        <div class="callout reveal mt-2">
          <div class="card-icon">{icon("alert")}</div>
          <p><strong>An important note.</strong> A rental valuation is a professional estimate based on the information available and comparable local evidence. It is intended as guidance to help you make an informed decision and is not a guarantee of achievable rent.</p>
        </div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Why Get a Valuation?</p>
          <h2 class="section-title">The Benefits of a Rental Valuation</h2>
        </div>
        <div class="grid grid-3">{benefits_html}</div>
      </div>
    </section>

    <section class="section section--light" id="valuation-form">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Get Started</p>
          <h2 class="section-title">Request Your Free Rental Valuation</h2>
          <p class="section-lead">Complete the form below and we'll be in touch with a professional estimate.</p>
        </div>
        <div style="max-width:860px;margin:0 auto" class="reveal">{valuation_form()}</div>
        <div class="btn-group mt-2" style="justify-content:center">
          <a class="btn btn--navy" href="{WA_LINK}" target="_blank" rel="noopener">{icon("chat","",18)} WhatsApp Us</a>
          <a class="btn btn--secondary" href="tel:{PHONE_TEL}">{icon("phone","",18)} Request a Callback</a>
        </div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Questions</p>
          <h2 class="section-title">Rental Valuation FAQs</h2>
        </div>
        <div class="faq-list">{val_faq_html}</div>
      </div>
    </section>

    {cta("Request Your Free Rental Valuation",
         "Find out what your property could rent for with a free, no-obligation professional estimate.",
         "Request Your Free Rental Valuation", "#valuation-form")}
  </main>
'''
    write("rental-valuation.html", page(
        "Free Rental Valuation | Ascend Lettings",
        "Request your free rental valuation from Ascend Lettings. Find out what your property could rent for with a professional, no-obligation estimate based on local evidence.",
        "rental-valuation.html", valuation_body, extra_schema=faq_schema(VAL_FAQS)))


    # ============================================================
    # TENANT REFERENCING
    # ============================================================
    ref_involves = [
        ("users", "Employment & Income", "Verification of employment and income to help assess whether the tenancy is affordable for the applicant."),
        ("trending", "Credit Checks", "A review of an applicant's credit history to help build a picture of their financial circumstances."),
        ("home", "Previous Landlord Reference", "Where applicable, a reference from a previous landlord or letting agent about the applicant's tenancy history."),
        ("shield", "Right to Rent", "Confirmation, explained separately, that the applicant has the legal right to rent property in England."),
    ]
    ref_involves_html = "".join(service_card(i, t, d) for i, t, d in ref_involves)
    ref_steps = [
        ("Application", "A prospective tenant applies and provides their details and documentation."),
        ("Checks", "We coordinate identity, affordability, employment and previous landlord checks."),
        ("Right to Rent", "We assist with confirming the applicant's right to rent in England."),
        ("Outcome", "We share the outcome with you so you can make an informed decision."),
    ]
    ref_steps_html = "".join(f'''<div class="step-card reveal"><span class="step-num">{i+1}</span><h4>{t}</h4><p>{d}</p></div>'''
                             for i, (t, d) in enumerate(ref_steps))

    referencing_body = f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / <a href="services.html">Services</a> / Tenant Referencing</p>
        <h1>Tenant Referencing &mdash; Helping Landlords Let With Confidence</h1>
        <p>Referencing helps assess a prospective tenant's suitability, giving landlords greater confidence in the tenancy.</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="split">
          <div class="reveal">
            <p class="eyebrow">What It Involves</p>
            <h2 class="section-title">What Tenant Referencing Involves</h2>
            <p>Tenant referencing is a standard part of the letting process. It typically brings together several checks to help assess whether a prospective tenant is suitable for a tenancy, including verification of employment and income, a review of credit history, and, where applicable, a reference from a previous landlord.</p>
            <p>Right to Rent is a separate legal check, explained on our <a href="right-to-rent.html">Right to Rent</a> page, which confirms an applicant's legal right to rent property in England.</p>
          </div>
          <div class="split-media reveal delay-1"><img src="{REFERENCING_IMG}" alt="A person reviewing tenancy paperwork at a desk"></div>
        </div>
        <div class="grid grid-4 mt-2">{ref_involves_html}</div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">Why It Matters</p>
          <h2 class="section-title">Why Referencing Matters</h2>
          <p class="section-lead">Referencing helps both landlords and tenants start a tenancy on a clear, informed footing.</p>
        </div>
        <div class="grid grid-3">
          <div class="card feature-card reveal"><div class="card-icon">{icon("shield")}</div><h4>Confidence for Landlords</h4><p>Referencing gives landlords greater confidence that a prospective tenant is suitable for the tenancy.</p></div>
          <div class="card feature-card reveal delay-1"><div class="card-icon">{icon("check")}</div><h4>A Clear Basis</h4><p>It provides a clear, consistent basis for making an informed letting decision.</p></div>
          <div class="card feature-card reveal delay-2"><div class="card-icon">{icon("users")}</div><h4>Fair to Everyone</h4><p>A standard process helps ensure prospective tenants are considered fairly and consistently.</p></div>
        </div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">The Process</p>
          <h2 class="section-title">The Referencing Process</h2>
        </div>
        <div class="grid grid-4 steps">{ref_steps_html}</div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="grid grid-2">
          <div class="card reveal">
            <div class="card-icon">{icon("home")}</div>
            <h3>What Landlords Can Expect</h3>
            <p>We coordinate the referencing process on your behalf and keep you informed. Once checks are complete, we share the outcome with you so you can make an informed decision about the tenancy.</p>
          </div>
          <div class="card reveal delay-1">
            <div class="card-icon">{icon("lifebuoy")}</div>
            <h3>Guidance for Tenants</h3>
            <p>If you're going through referencing, it helps to have your identification, proof of address and proof of income or employment ready. We'll let you know what's required and guide you through each step.</p>
          </div>
        </div>
        <div class="callout reveal mt-2">
          <div class="card-icon">{icon("info")}</div>
          <p><strong>Please note.</strong> Referencing is conducted in line with applicable regulations. The information on this page is general guidance only and is not legal advice. For advice on your specific circumstances, please consult a suitably qualified professional.</p>
        </div>
      </div>
    </section>

    {cta("Let With Confidence",
         "Start the letting process and let us coordinate referencing on your behalf.",
         "Start the Letting Process", "landlords.html#landlord-form")}
  </main>
'''
    write("tenant-referencing.html", page(
        "Tenant Referencing | Ascend Lettings",
        "Tenant referencing from Ascend Lettings helps landlords let with confidence \u2014 covering employment, income, credit checks and previous landlord references. General guidance, not legal advice.",
        "tenant-referencing.html", referencing_body))

    # ============================================================
    # RIGHT TO RENT
    # ============================================================
    rtr_landlord = [
        ("file", "What the Checks Involve", "Right to Rent checks involve confirming that a prospective tenant has the legal right to rent property in England, usually by checking original documents or using an approved online checking method."),
        ("book", "Types of Documents", "Acceptable documents can include a passport, immigration documentation or other approved forms of evidence. The current government guidance sets out which documents are acceptable."),
        ("calendar", "Timing", "Checks generally need to be carried out before the start of a tenancy, and in some cases follow-up checks may be required. We assist in coordinating this at the right time."),
    ]
    rtr_landlord_html = "".join(service_card(i, t, d) for i, t, d in rtr_landlord)
    rtr_tenant = [
        ("info", "What to Expect", "As part of your application you'll be asked to demonstrate your right to rent in England. This is a standard requirement and applies to prospective tenants."),
        ("file", "Documents to Prepare", "It helps to have appropriate identification and any relevant immigration documentation ready. We'll let you know which documents are acceptable for your circumstances."),
        ("chat", "We'll Guide You", "We'll explain what's needed and support you through the check, so the process is as straightforward as possible."),
    ]
    rtr_tenant_html = "".join(service_card(i, t, d) for i, t, d in rtr_tenant)

    right_to_rent_body = f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / <a href="services.html">Services</a> / Right to Rent</p>
        <h1>Right to Rent &mdash; Understanding Your Obligations</h1>
        <p>General guidance on Right to Rent for landlords and tenants, and how we help you meet this requirement.</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">The Basics</p>
          <h2 class="section-title">What Is Right to Rent?</h2>
          <p class="section-lead">Right to Rent is a UK government requirement for landlords to check that tenants have the legal right to rent property in England before a tenancy begins. As part of our letting service, we assist with obtaining and verifying the appropriate documentation.</p>
        </div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">For Landlords</p>
          <h2 class="section-title">Guidance for Landlords</h2>
          <p class="section-lead">What the checks involve, the kinds of documents used, and when checks are carried out.</p>
        </div>
        <div class="grid grid-3">{rtr_landlord_html}</div>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="section-head center reveal">
          <p class="eyebrow">For Tenants</p>
          <h2 class="section-title">Guidance for Tenants</h2>
          <p class="section-lead">What to expect and how to prepare for your Right to Rent check.</p>
        </div>
        <div class="grid grid-3">{rtr_tenant_html}</div>
      </div>
    </section>

    <section class="section section--light">
      <div class="container">
        <div class="callout reveal">
          <div class="card-icon">{icon("alert")}</div>
          <p><strong>Important:</strong> The information on this page is general guidance only and is not legal advice. Right to Rent rules can change, so you should always consult the current official government guidance. For advice on your specific circumstances, please consult a suitably qualified professional. You can find the official guidance on the UK government website at <a href="https://www.gov.uk/" target="_blank" rel="noopener">gov.uk</a>.</p>
        </div>
      </div>
    </section>

    {cta("Let Your Property With Confidence",
         "We assist with Right to Rent as part of our professional letting service.",
         "Start the Letting Process", "landlords.html#landlord-form")}
  </main>
'''
    write("right-to-rent.html", page(
        "Right to Rent \u2014 Understanding Your Obligations | Ascend Lettings",
        "General guidance on Right to Rent for landlords and tenants in England. Ascend Lettings assists with obtaining and verifying the appropriate documentation. Not legal advice.",
        "right-to-rent.html", right_to_rent_body))


    # ============================================================
    # LEGAL PAGES
    # ============================================================
    UPDATED = "August 2026"

    def legal_page(breadcrumb, title, intro, content_html, review_note=None):
        note = (f'''<div class="callout reveal mt-2">
          <div class="card-icon">{icon("alert")}</div>
          <p><strong>Please note:</strong> {review_note}</p>
        </div>''' if review_note else "")
        return f'''  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="breadcrumb"><a href="index.html">Home</a> / {breadcrumb}</p>
        <h1>{title}</h1>
        <p>{intro}</p>
      </div>
    </section>

    <section class="section section--white">
      <div class="container">
        <div class="legal-content reveal">
          <p class="legal-updated">Last updated: {UPDATED}</p>
          {content_html}
          {note}
        </div>
      </div>
    </section>
  </main>
'''

    # ---------- PRIVACY POLICY ----------
    privacy_content = f'''
      <h2>1. Who We Are</h2>
      <p>This Privacy Policy explains how Ascend Lettings ("we", "us", "our") collects, uses and protects your personal information when you use our website or enquire about our letting services. Ascend Lettings is the data controller responsible for your personal information.</p>
      <p>Ascend Lettings is registered with the Information Commissioner's Office (ICO) and is ICO certified. If you have any questions about this policy or how we handle your data, please contact us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

      <h2>2. What Data We Collect</h2>
      <p>We may collect and process the following categories of personal information:</p>
      <ul>
        <li><strong>Enquiry information:</strong> details you provide through our enquiry, valuation, registration and contact forms, such as your name, email address, telephone number, property address and the content of your message.</li>
        <li><strong>Website usage information:</strong> limited technical information collected through your browser, and, where you consent, website analytics data about how you use our site.</li>
      </ul>
      <p>We do not knowingly collect more information than we need, and we do not sell your personal information.</p>

      <h2>3. How We Use Your Data</h2>
      <p>We use your personal information to:</p>
      <ul>
        <li>respond to your enquiries and provide the letting services you request;</li>
        <li>communicate with you about your enquiry, valuation or requirements;</li>
        <li>maintain records of our correspondence and interactions; and</li>
        <li>improve our website and understand how it is used, where you have consented to analytics.</li>
      </ul>

      <h2>4. Legal Basis for Processing</h2>
      <p>Under the UK General Data Protection Regulation (UK GDPR), we rely on the following legal bases:</p>
      <ul>
        <li><strong>Consent:</strong> where you have agreed to us contacting you or to non-essential cookies such as analytics.</li>
        <li><strong>Legitimate interests:</strong> to respond to enquiries and operate our business in a professional manner.</li>
        <li><strong>Legal obligation:</strong> where we are required to process information to comply with the law.</li>
      </ul>

      <h2>5. Data Retention</h2>
      <p>We keep your personal information only for as long as necessary to fulfil the purposes for which it was collected, including to meet any legal, accounting or reporting requirements. When your information is no longer required, we take reasonable steps to delete or anonymise it.</p>

      <h2>6. Your Rights</h2>
      <p>Under UK GDPR, you have rights in relation to your personal information, including the right to:</p>
      <ul>
        <li>access the personal information we hold about you;</li>
        <li>request correction of inaccurate information;</li>
        <li>request erasure of your information in certain circumstances;</li>
        <li>object to or restrict our processing of your information; and</li>
        <li>withdraw consent at any time where we rely on consent.</li>
      </ul>
      <p>To exercise any of these rights, please contact us at <a href="mailto:{EMAIL}">{EMAIL}</a>. You also have the right to lodge a complaint with the ICO if you are unhappy with how we have handled your information.</p>

      <h2>7. Cookies</h2>
      <p>Our website uses cookies. For more information, please see our <a href="cookie-policy.html">Cookie Policy</a>.</p>

      <h2>8. Contact for Data Queries</h2>
      <p>If you have any questions about this Privacy Policy or wish to exercise your data protection rights, please contact us:</p>
      <ul>
        <li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>Phone: <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
      </ul>
    '''
    write("privacy-policy.html", page(
        "Privacy Policy | Ascend Lettings",
        "How Ascend Lettings collects, uses and protects your personal information in line with UK GDPR, including your data rights and how to contact us about data queries.",
        "privacy-policy.html",
        legal_page("Privacy Policy", "Privacy Policy",
                   "How we collect, use and protect your personal information in line with UK GDPR.",
                   privacy_content,
                   review_note="This policy is provided as a general template and should be reviewed by a legal professional before publishing.")))

    # ---------- COOKIE POLICY ----------
    cookie_content = f'''
      <h2>1. What Are Cookies?</h2>
      <p>Cookies are small text files that are placed on your device when you visit a website. Similar technologies, such as browser local storage, can also be used to store small amounts of information. They help websites function, remember your preferences and understand how the site is used.</p>

      <h2>2. Types of Cookies</h2>
      <ul>
        <li><strong>Essential cookies:</strong> necessary for the website to function and to remember your cookie preferences. These cannot be switched off in our systems.</li>
        <li><strong>Analytics cookies:</strong> help us understand how visitors interact with our website so we can improve it. These are only used where you have given consent.</li>
        <li><strong>Functional cookies:</strong> enable enhanced functionality and personalisation. These are only used where relevant and, where required, with your consent.</li>
      </ul>

      <h2>3. Cookies We Currently Use</h2>
      <p>At present, our website uses <strong>essential cookies only</strong>. Your cookie consent preference is stored locally in your browser's local storage so that we can remember your choice and avoid showing the cookie banner on every visit. This preference is stored on your device and is not used to track you across other websites.</p>

      <h2>4. Analytics (Placeholder)</h2>
      <p>We may introduce website analytics in the future to help us understand how our site is used and to improve it. If we do, analytics such as Google Analytics would only be enabled where you have opted in through our cookie banner. This policy will be updated to reflect any such change before analytics are enabled.</p>

      <h2>5. How to Manage Your Cookie Preferences</h2>
      <p>You can manage cookies in the following ways:</p>
      <ul>
        <li><strong>Our cookie banner:</strong> when you first visit, you can accept or reject non-essential cookies. You can clear your browser's local storage to be shown the banner again.</li>
        <li><strong>Your browser settings:</strong> most browsers let you view, manage and delete cookies, and block cookies from being set. Please refer to your browser's help pages for instructions.</li>
      </ul>
      <p>Please note that blocking essential cookies may affect how the website functions.</p>

      <h2>6. More Information</h2>
      <p>For more about how we handle your personal information, please see our <a href="privacy-policy.html">Privacy Policy</a>. If you have any questions about our use of cookies, please contact us at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
    '''
    write("cookie-policy.html", page(
        "Cookie Policy | Ascend Lettings",
        "How Ascend Lettings uses cookies. We currently use essential cookies only, with your consent preference stored in your browser. Learn how to manage your preferences.",
        "cookie-policy.html",
        legal_page("Cookie Policy", "Cookie Policy",
                   "How we use cookies and similar technologies on our website.",
                   cookie_content)))

    # ---------- TERMS & CONDITIONS ----------
    terms_content = f'''
      <h2>1. About These Terms</h2>
      <p>These Terms and Conditions govern your use of the Ascend Lettings website. By accessing or using our website, you agree to these terms. If you do not agree, please do not use the website.</p>

      <h2>2. Use of the Website</h2>
      <p>You may use our website for lawful purposes only. You agree not to use the website in any way that is unlawful, that could damage or impair the site, or that interferes with any other party's use of the website. The content on this website is provided for general information about our letting services.</p>

      <h2>3. Services Terms</h2>
      <p>Information about our services is provided for general guidance and does not constitute a formal contract or an offer capable of acceptance. Any letting services we provide will be subject to separate agreement and any applicable terms provided to you at the time. Ascend Lettings is a letting agency and does not currently offer ongoing property management services such as rent collection, maintenance or inspections.</p>

      <h2>4. No Advice</h2>
      <p>Content on this website is general information only and does not constitute legal, financial or professional advice. You should seek appropriate professional advice for your specific circumstances before making decisions.</p>

      <h2>5. Limitation of Liability</h2>
      <p>While we take reasonable care to ensure the information on our website is accurate and up to date, we make no representations or warranties of any kind, express or implied, about the completeness, accuracy or reliability of the content. To the fullest extent permitted by law, we exclude liability for any loss or damage arising from your use of, or reliance on, this website. Nothing in these terms excludes or limits liability that cannot be excluded or limited under applicable law.</p>

      <h2>6. Intellectual Property</h2>
      <p>All content on this website, including text, graphics, logos and imagery, is owned by or licensed to Ascend Lettings and is protected by applicable intellectual property laws. You may not reproduce, distribute or otherwise use our content without our prior written permission.</p>

      <h2>7. Third-Party Links</h2>
      <p>Our website may contain links to third-party websites. These links are provided for convenience only. We have no control over the content of those websites and accept no responsibility for them.</p>

      <h2>8. Governing Law</h2>
      <p>These terms are governed by and construed in accordance with the laws of England and Wales, and any disputes will be subject to the exclusive jurisdiction of the courts of England and Wales.</p>

      <h2>9. Contact</h2>
      <p>If you have any questions about these terms, please contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or on <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>.</p>
    '''
    write("terms.html", page(
        "Terms & Conditions | Ascend Lettings",
        "The terms and conditions governing use of the Ascend Lettings website, including limitation of liability, intellectual property and governing law (England and Wales).",
        "terms.html",
        legal_page("Terms &amp; Conditions", "Terms &amp; Conditions",
                   "The terms that govern your use of the Ascend Lettings website.",
                   terms_content,
                   review_note="These terms are provided as a general template and should be reviewed by a legal professional before publishing.")))

    # ---------- COMPLAINTS ----------
    complaint_include = [
        "Your name and preferred contact details",
        "The property or service your complaint relates to",
        "A clear description of what went wrong and when",
        "Copies of any relevant correspondence or documents",
        "What you would like us to do to put things right",
    ]
    complaint_include_html = "".join(f'<li>{icon("check","",20)} {t}</li>' for t in complaint_include)
    complaints_content = f'''
      <p>We are committed to providing a professional service to all our clients. If something has not met your expectations, we want to hear about it so we can put it right. We take all complaints seriously and aim to handle them fairly, promptly and transparently.</p>

      <h2>Step 1: Contact Us Directly</h2>
      <p>In the first instance, please get in touch with us so we can try to resolve your concern quickly and informally. You can reach us by email at <a href="mailto:{EMAIL}">{EMAIL}</a> or by phone on <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>. Many concerns can be resolved at this stage.</p>

      <h2>Step 2: Make a Written Complaint</h2>
      <p>If your concern is not resolved, or you would prefer to put it in writing, please send us a written complaint by email to <a href="mailto:{EMAIL}">{EMAIL}</a>. We will acknowledge your written complaint promptly and carry out a full and fair investigation. We will then provide you with a written response setting out our findings and any proposed resolution.</p>

      <h2>Step 3: Escalation to the Property Redress Scheme</h2>
      <p>Ascend Lettings is a Property Redress Scheme member. If you remain dissatisfied once our internal complaints process has been completed, or if we have been unable to resolve your complaint within the applicable timeframe, you may be entitled to refer your complaint to the Property Redress Scheme for independent review.</p>
      <p>Property Redress Scheme contact details: [PROPERTY REDRESS SCHEME CONTACT INFORMATION].</p>

      <h2>Response Timeframes</h2>
      <ul>
        <li>We aim to acknowledge written complaints within a few working days of receipt.</li>
        <li>We aim to provide a full written response within a reasonable period following our investigation.</li>
        <li>If we need more time to investigate fully, we will let you know and keep you updated.</li>
      </ul>

      <h2>What to Include in Your Complaint</h2>
      <p>To help us investigate and respond effectively, please include the following where possible:</p>
      <ul class="check-list">{complaint_include_html}</ul>

      <p class="mt-2">We appreciate you taking the time to let us know when something is not right. Your feedback helps us maintain and improve the standard of our service.</p>
    '''
    write("complaints.html", page(
        "Complaints Procedure | Ascend Lettings",
        "Ascend Lettings' complaints procedure. Contact us directly, make a written complaint, and, if needed, escalate to the Property Redress Scheme. We handle complaints fairly and promptly.",
        "complaints.html",
        legal_page("Complaints Procedure", "Complaints Procedure",
                   "How to raise a complaint with us and how we handle it, fairly and professionally.",
                   complaints_content)))
