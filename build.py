import os, html
NOINDEX = True  # set False at launch
PHONE, EMAIL = "303-903-5873", "contact@apsland.com"
SV = [("seismic-permitting","Seismic Permitting"),("right-of-way-acquisition","Right-of-Way Acquisition"),("title-leasing","Title and Leasing"),("gis","GIS Services")]
SVD = {
"seismic-permitting":"Land access and permitting for 2D, 3D, and 4D seismic surveys, microseismic, and VSP programs, and for CCUS, solar, data-center, and other complex field projects. Seismic permitting has been the core of APS's work for more than 45 years.",
"right-of-way-acquisition":"Permanent and temporary easements, workspace, and access agreements for pipelines, electric transmission, utilities, telecommunications, and roads, from corridor ownership and title review through tract-by-tract acquisition and agreement execution.",
"title-leasing":"Surface and mineral ownership research at any stage of a project, including title searches to sovereignty, probate and heirship research, title curative, and lease negotiation and acquisition.",
"gis":"Project maps and databases connecting ownership and title information to the land, with legal description and tract platting, spatial data compilation and reconciliation, and project database development."}
def ul(items): return '<ul class="ck">'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'
def head(depth):
    p='../'*depth
    dd=''.join(f'<a href="{p}services/{s}/">{n}</a>' for s,n in SV)
    return f'''<header class="hdr"><div class="wrap"><a class="logo" href="{p or './'}"><img src="{p}assets/logo.png" alt="APS Land Services" width="163" height="46"></a>
<button class="burger" aria-label="Menu" aria-expanded="false">&#9776;</button>
<nav class="nav" aria-label="Main"><div class="dd"><a href="{p}services/">Services</a><div class="dd-menu">{dd}</div></div>
<a href="{p}about/">About</a><a href="{p}safety/">Safety and HSE</a><a href="{p}landowners/">Landowners</a><a class="cta" href="{p}contact/">Contact</a></nav></div></header>'''
def foot(depth):
    p='../'*depth
    sv=''.join(f'<a href="{p}services/{s}/">{n}</a>' for s,n in SV)
    return f'''<footer class="ftr"><div class="wrap"><div class="grid"><div><img src="{p}assets/logo.png" alt="APS Land Services"><p>Utah | Montana | Texas</p></div>
<div><h4>Services</h4>{sv}</div><div><h4>Company</h4><a href="{p}about/">About</a><a href="{p}safety/">Safety and HSE</a><a href="{p}landowners/">Landowners</a><a href="{p}contact/">Contact</a></div>
<div><h4>Contact</h4><a href="tel:{PHONE}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
<div class="copy">&copy; 2026 APS Land Services. All rights reserved. <a href="{p}privacy/">Privacy Policy</a></div></div></footer>'''
def page(path,title,desc,body,depth,extra=''):
    p='../'*depth
    robots='<meta name="robots" content="noindex,nofollow">' if NOINDEX else ''
    out=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">{robots}
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="website">
<meta name="theme-color" content="#1B2F5B">
<link rel="icon" href="{p}favicon.ico"><link rel="icon" type="image/png" sizes="32x32" href="{p}favicon-32x32.png"><link rel="icon" type="image/png" sizes="16x16" href="{p}favicon-16x16.png">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png"><link rel="manifest" href="{p}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Source+Serif+4:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css"></head><body><a class="skip" href="#main">Skip to content</a>
{head(depth)}<main id="main">{body}</main>{foot(depth)}<script src="{p}assets/main.js"></script>{extra}</body></html>'''
    d=os.path.join(*path.split('/')) if path else ''
    os.makedirs(d or '.',exist_ok=True)
    open(os.path.join(d,'index.html'),'w').write(out)
def phead(h,sub=''): return f'<div class="phead"><div class="wrap narrow" style="max-width:1140px"><h1>{h}</h1>{sub}</div></div>'
CTA=lambda p:f'<p style="margin-top:32px"><a class="btn navy" href="{p}contact/">Contact APS</a></p>'

# HOME
cards=''.join(f'<a class="card fade" href="services/{s}/"><h3>{n}</h3><p>{SVD[s]}</p><span class="more">Learn more &rarr;</span></a>' for s,n in SV)
home=f'''<section class="hero"><div class="wrap"><h1>APS Land Services</h1>
<p>Seismic permitting, right-of-way acquisition, title and leasing, and GIS services for energy and infrastructure projects.</p>
<p class="engage">Engage APS for a single service or for work across a project's lifecycle.</p>
<div class="btns"><a class="btn" href="contact/">Contact APS</a><a class="btn ghost" href="services/">View services</a></div></div></section>
<section><div class="wrap"><div class="eyebrow">What we do</div><h2>Services</h2><div class="grid g4">{cards}</div></div></section>
<section class="alt" id="footprint"><div class="wrap mapbox"><div class="fade"><div class="eyebrow">Experience</div><h2>Project experience</h2>
<p>APS has supported hundreds of energy and infrastructure projects across North America and conducted thousands of negotiations involving right-of-way, leasing, permitting, land access, and other property rights. Project experience spans 28 states plus Alberta and Saskatchewan, across private, state, federal, and tribal lands.</p>
<p class="stat">Three locations: Utah, Montana, and Texas.</p></div>
<div class="mapwrap"><div id="us-map"></div><div id="map-state-panel" aria-live="polite"><span id="msp-name"></span></div>
<div class="legend"><span><i style="background:var(--navy)"></i>Project experience</span><span><i style="background:var(--red);border-radius:50%"></i>APS location</span></div></div></div></section>
<section><div class="wrap"><div class="eyebrow">How we work</div><h2>Project management</h2><div class="grid g3">
<div class="card plain fade"><p style="color:var(--ink)">Senior leadership is engaged on every project. Personnel are vetted and experienced, and communication is handled directly by APS.</p></div>
<div class="card plain fade"><p style="color:var(--ink)">Title, GIS, acquisition, and field data are reconciled, with discrepancies tracked and resolved. Progress reports are clear and consistent.</p></div>
<div class="card plain fade"><p style="color:var(--ink)">Scope, specifications, and deliverables are defined upfront. Critical timelines are actively managed and consistently reported. Pricing is flexible: turnkey, unit, or project-based.</p></div></div></div></section>
<section class="alt"><div class="wrap cols"><div><div class="eyebrow">Safety</div><h2>Safety</h2></div><div><p>Work follows the APS Safety Program Manual, the Injury and Illness Prevention Program, and applicable client and project requirements. APS is a member of ISNetworld.</p><a class="btn navy" href="safety/">Safety and HSE</a></div></div></section>
<section class="band"><div class="wrap cols"><div><h2>Contact</h2></div><div><a class="big" href="tel:{PHONE}">{PHONE}</a><a class="big" style="font-size:1.4rem;margin-top:6px" href="mailto:{EMAIL}">{EMAIL}</a></div></div></section>'''
page('','APS Land Services | Seismic, Right-of-Way, Title & GIS','Seismic permitting, right-of-way acquisition, title and leasing, and GIS services for energy and infrastructure projects. '+PHONE+'.',home,0,'<script src="assets/us-map.js"></script>')

# SERVICES HUB
disc=''.join(f'<a class="card" href="{s}/"><h3>{n}</h3><p>{d}</p><span class="more">Learn more &rarr;</span></a>' for (s,n),d in zip(SV,["Land access, permitting, approvals, and field compliance","Easements and linear property rights for infrastructure corridors","Surface and mineral ownership research, title curative, and leasing","Project maps, databases, and data reconciliation"]))
hub=phead('Services')+f'''<section><div class="wrap"><p class="lead narrow">APS provides four land services disciplines, engaged individually or in related scopes, from preliminary research and mapping through access negotiations, acquisition, and field oversight.</p></div></section>
<section class="alt" style="padding-top:64px"><div class="wrap"><h2>Engagement options</h2><div class="grid g3">
<div class="card plain"><h3>A single service</h3><p>A seismic permitting program, a right-of-way scope, a title research assignment, or a mapping and database project can each be engaged on its own.</p></div>
<div class="card plain"><h3>Related scopes</h3><p>Ownership research, mapping, acquisition, and field work can be engaged together, with the information coordinated across disciplines.</p></div>
<div class="card plain"><h3>Project review</h3><p>For a project experiencing difficulties, consult with APS leadership to diagnose obstacles, restore control, and establish a clear path forward.</p></div></div></div></section>
<section><div class="wrap"><h2>The disciplines</h2><div class="grid g4">{disc}</div>{CTA('../')}</div></section>'''
page('services','Land Services | APS Land Services','Seismic permitting, right-of-way acquisition, title and leasing, and GIS services for energy and infrastructure projects nationwide.',hub,1)

# SERVICE PAGES (title, meta, intro, [(h2, para|list)])
S={
"seismic-permitting":("Seismic Permitting | APS Land Services","Land access and permitting for 2D, 3D, and 4D seismic, microseismic, and VSP programs, plus CCUS, solar, and data-center field projects.",
 "Seismic permitting has been at the core of APS's work for more than 45 years. APS manages land access for 2D, 3D, and 4D seismic surveys, microseismic, and VSP programs, and for CCUS, solar, data-center, and other complex field projects.",
 [("Landowner contact and conditions",["Every property presents its own conditions. Access routes, crops and livestock, hunting seasons, fences, water wells, existing infrastructure, environmental restrictions, compensation, and potential damages can all affect where and how field operations are conducted.","APS contacts landowners personally to explain who APS represents, what the project involves, what access is being requested, and how the property will be used. Conditions are negotiated with the landowner, documented in the agreement, and carried into the field, where APS oversees compliance to protect all parties and the client's reputation."]),
  ("Approvals and administration",["APS coordinates applicable municipal, county, state, and federal approvals. Permit status is tracked and reported throughout the program. APS handles landowner payments, check processing, and required IRS filings, and coordinates surface damage settlement."]),
  ("Early involvement",["Preliminary ownership research can reveal who controls the surface and minerals, how ownership is divided, where access may be difficult, and how many interests need to be addressed, before significant resources are committed."])],
 ["title-leasing","gis"]),
"right-of-way-acquisition":("Right-of-Way Acquisition | APS Land Services","Easements and property rights for pipelines, transmission, utilities, and roads, with ownership, GIS, and acquisition status coordinated as routes change.",
 "APS secures linear property rights for pipelines, electric transmission, utilities, telecommunications, roads, and other critical infrastructure. Work includes verifying corridor ownership and existing rights, identifying affected tracts and encumbrances, contacting landowners personally, negotiating compensation and property terms, and executing easement and access agreements.",
 [("Alignment changes",["ROW acquisition develops alongside the route. A rejected agreement, divided interest, existing easement, utility conflict, or physical constraint can change an alignment after acquisition is underway, and a reroute can introduce new parcels, owners, title questions, mapping, and negotiations. APS identifies these conflicts early and keeps ownership, GIS, acquisition status, and route changes synchronized as the corridor develops."]),
  ("Property rights",["Permanent and temporary easements","Temporary and additional workspace","Ingress, egress, and access agreements","Property restrictions and restoration terms"]),
  ("Acquisition",["Corridor ownership, title, and encumbrance review","Landowner negotiation and compensation","Tract acquisition tracking and reporting","Agreement execution and documentation","Agency, utility, and crossing coordination"])],[]),
"title-leasing":("Title and Leasing | APS Land Services","Surface and mineral ownership research, title searches to sovereignty, probate and heirship research, title curative, and lease negotiation and acquisition.",
 "APS researches surface and mineral ownership at any stage of a project, from early feasibility through active negotiation and acquisition. Preliminary research can reveal who controls the surface and minerals, how ownership is divided, where access may be difficult, and how many interests need to be addressed, before significant resources are committed.",
 [("Ownership records",["Surface and mineral estates may have separated generations ago. Interests may be divided among multiple heirs, and federal, state, or tribal lands can involve separate records and approval requirements. APS traces and reconciles chains of title through county and parish courthouses, federal, state, and tribal land systems, and recorded instruments and historical archives, then maintains the information for use in GIS mapping, negotiations, acquisition, and field operations."]),
  ("Services",["Full title search to sovereignty","Surface and mineral ownership","Probate, heirship, and fractional interests","Title curative","Lease research, negotiation, and acquisition"])],[]),
"gis":("GIS Services | APS Land Services","Project maps and databases connecting ownership and title information to the land, with spatial data compilation, reconciliation, and tract platting.",
 "APS builds project maps and databases that connect ownership and title information to the land. Surface and mineral ownership, leases, legal descriptions, topography, crops, infrastructure, project boundaries, and other relevant data are compiled and organized geographically for planning, negotiating use agreements, acquisition, and field use.",
 [("Data reconciliation",["Surface and mineral interests do not always follow the same boundaries. Historical legal descriptions may not align with current parcels, and a change in project alignment can introduce a different set of affected properties. APS reconciles those differences across the project mapping and supporting data, keeping the information organized and current as the work develops."]),
  ("Services",["Comprehensive project mapping","Legal description and tract platting","Spatial data compilation and reconciliation","Project database development and management","Maps and exhibits"])],[])}
NAMES=dict(SV)
for slug,(t,d,intro,secs,rel) in S.items():
    b=''.join(f'<h2>{h}</h2>'+(ul(c) if len(c)>1 and len(c[0])<70 else ''.join(f'<p>{x}</p>' for x in c)) for h,c in secs)
    r=''
    if rel: r='<p><strong>Related services:</strong> '+', '.join(f'<a href="../{x}/">{NAMES[x]}</a>' for x in rel)+'.</p>'
    page(f'services/{slug}',t,d,phead(NAMES[slug])+f'<section><div class="wrap narrow prose"><p class="lead">{intro}</p>{b}{r}{CTA("../../")}</div></section>',2)

# ABOUT
about=phead('About APS Land Services')+f'''<section><div class="wrap narrow prose"><p class="lead">APS Land Services provides land services for energy, exploration, and infrastructure projects.</p>
<p>APS has supported hundreds of energy and infrastructure projects across North America and conducted thousands of negotiations involving right-of-way, leasing, permitting, land access, and other property rights. Project experience spans difficult jurisdictions, challenging access, and demanding field conditions across private, state, federal, and tribal lands in 28 states, plus Alberta and Saskatchewan.</p>
<p>The company focuses on getting the details right and delivering on time, and takes pride in protecting landowners, field crews, the environment, and the projects entrusted to it.</p><p>Three locations: Utah, Montana, and Texas.</p></div></section>
<section class="alt"><div class="wrap"><h2>Leadership</h2><div style="max-width:900px">
<div class="person"><img src="../assets/mark.jpg" alt="Mark Fischbuch" loading="lazy"><div><h3>Mark Fischbuch</h3><div class="eyebrow">President and Founder</div><p>Mark Fischbuch began working in the seismic industry in 1980, gaining experience in various positions throughout field operations. He built his own company, drawing on that background to improve the research, information gathering, and land access processes that too often delayed field work. Decades of ownership research, landowner negotiations, and oversight of field operations continue to shape how APS works.</p></div></div>
<div class="person" style="margin-bottom:0"><img src="../assets/zane.jpg" alt="Zane Nelson" loading="lazy"><div><h3>Zane Nelson</h3><div class="eyebrow">Vice President</div><p>Zane Nelson joined APS in 2010 after distinguishing himself as a leader in geoscience business operations. He first served as CFO, transforming the company's financial structure, then took on project leadership and responsibility for day-to-day operations. As Vice President he oversees operations, works closely with clients and project teams, and continues to drive the company's growth.</p></div></div></div></div></section>'''
page('about','About APS Land Services','APS Land Services is a land services company serving energy and infrastructure projects, led by Mark Fischbuch and Zane Nelson.',about,1)

# SAFETY
page('safety','Safety and HSE | APS Land Services','HSE compliance and accident prevention: safety program manual, IIPP, daily safety briefings, JSAs, and stop-work authority. ISNetworld member.',
 phead('Safety and HSE')+f'''<section><div class="wrap narrow prose"><p class="lead">APS personnel are accountable for health, safety, and environmental (HSE) compliance and accident prevention. Work follows the APS Safety Program Manual, the Injury and Illness Prevention Program (IIPP), and applicable client and project requirements.</p>
<p>In the field, APS personnel participate in daily safety briefings and job safety analyses (JSAs), monitor operations for compliance, and exercise stop-work authority when field conditions or activities fall outside established requirements.</p>
<p>APS Land Services is a member of ISNetworld.</p><p>Procurement and contractor-management questions: <a href="tel:{PHONE}">{PHONE}</a>, <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>''',1)

# LANDOWNERS
page('landowners','Landowners | APS Land Services','Contacted by APS? Here is who we are, what to expect, and how to reach APS directly.',
 phead('Landowners')+f'''<section><div class="wrap narrow prose"><p class="lead">APS Land Services works with energy and infrastructure companies to secure land access for seismic surveys, pipelines, electric transmission, and similar projects.</p>
<p>If an APS representative has contacted you, they can explain the project, who APS represents, and what access is being requested. Agreed property conditions are documented in writing, and APS oversees field compliance with project requirements.</p>
<p>If you have questions about an agreement or a project, contact APS directly:</p>
<a class="big" href="tel:{PHONE}">{PHONE}</a><a class="big" style="font-size:1.4rem" href="mailto:{EMAIL}">{EMAIL}</a>
<p style="margin-top:28px;color:var(--mute);font-size:.9rem">General information only, not legal advice.</p></div></section>''',1)

# CONTACT
page('contact','Contact | APS Land Services','Contact APS Land Services about a project or a landowner matter. '+PHONE+', '+EMAIL+'.',
 phead('Contact')+f'''<section><div class="wrap"><div class="grid g3">
<div class="card"><h3>Project inquiries</h3><p style="color:var(--ink)">Call or email. You will speak directly with APS leadership. Useful details include project type, location, approximate timeline, the current stage of the work, and the scope you are considering.</p><a class="big" style="font-size:1.5rem" href="tel:{PHONE}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
<div class="card"><h3>Landowners</h3><p style="color:var(--ink)">Contacted by APS? See <a href="../landowners/">Landowners</a>.</p></div>
<div class="card"><h3>Procurement and contractor management</h3><p style="color:var(--ink)">APS is a member of ISNetworld. For contractor-management and safety-program questions, contact APS leadership.</p></div></div></div></section>''',1)

# PRIVACY (placeholder), 404, manifest, robots
page('privacy','Privacy Policy | APS Land Services','Privacy Policy for APS Land Services.',phead('Privacy Policy')+'<section><div class="wrap narrow prose"><!-- TODO: policy content required before launch --><p>Privacy policy content to be added before launch.</p></div></section>',1)
open('404.html','w').write(open('privacy/index.html').read().replace('../','/').replace('Privacy Policy | ','Page not found | ').replace('<h1>Privacy Policy</h1>','<h1>Page not found</h1>').replace('Privacy policy content to be added before launch.','That page does not exist. <a href="/">Return home</a>.'))
open('site.webmanifest','w').write('{"name":"APS Land Services","short_name":"APS Land","icons":[{"src":"android-chrome-192x192.png","sizes":"192x192","type":"image/png"},{"src":"android-chrome-512x512.png","sizes":"512x512","type":"image/png"}],"theme_color":"#1B2F5B","background_color":"#ffffff","display":"standalone"}')
open('.nojekyll','w').write('')
open('README.md','w').write('# APS Land Services site\nStatic site for GitHub Pages. Push to a repo, then Settings > Pages > deploy from branch (root).\nEdit content in `build.py` and run `python3 build.py`, or edit the HTML directly.\nTest builds carry `noindex`; set `NOINDEX = False` in `build.py` before launch.\n')
