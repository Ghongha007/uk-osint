# Research notes (checked 2026-11-23, via curl from outside UK government networks)

## Part A: companies, political money, spending, courts, Parliament, sanctions, FOI, outlets

94 entries in part_a.json. Each URL was fetched one request at a time with curl (browser User-Agent, -L, -m 20).

## Changed / moved
- OFSI Consolidated List closed on 28 Jan 2026. The UK Sanctions List (FCDO) is now the only official list. The OFSI search app still loads, with a banner saying it covers designations up to 28 Jan 2026 only. Both are listed, and the OFSI one is marked archived.
- Serious Fraud Office: sfo.gov.uk did not respond, so we use the GOV.UK organisation page (status "changed").
- Under the Procurement Act 2023 (from 24 Feb 2025), Find a Tender is the Central Digital Platform. Contracts Finder still loads but mostly holds legacy notices.
- Written questions API: writtenquestions-api.parliament.uk now redirects to questions-statements-api.parliament.uk.
- data.parliament.uk redirects to explore.data.parliament.uk. The Members' Names Data Platform path still works.
- register.openownership.org redirects to an Open Ownership explainer page, so the standalone register looks retired. Not listed as a source; only mentioned in the Open Ownership note.
- Isle of Man registry moved to services.gov.im/companies-registry (minor path change, status ok).
- British Newspaper Archive .co.uk redirects to .com (the .com URL is used).
- data.gov.uk is now branded "National Data Library". Not used in this half; flag it for the statistics category.

## Unreachable (17, kept because they are major sources)
- parliament.uk family behind a Cloudflare bot check: Commons interests register, Lords interests, APPG register, Hansard, Bills, Written questions, Committees, Public Accounts Committee. The parliament APIs (members-, interests-, bills-, committees-, questions-statements-api) all loaded, and the notes mention them.
- BAILII and legislation.gov.uk (bot checks; legislation returned an empty 202).
- Transparency International UK, Good Law Project and WhatDoTheyKnow (Cloudflare).
- TheyWorkForYou (429, then 503; mysociety.org also returned 503, which looks like a temporary outage).
- GrantNav (429 rate limit; 360giving.org loaded).
- Guernsey Registry greg.gg (503 "MyGov in Maintenance").
- British Newspaper Archive (security check).

## Dropped and why
- Individual Insolvency Register (insolvencydirect): personal bankruptcy lookup of private individuals, so out of scope. Disqualified directors kept, because they are company officers.
- Companies House bulk company data and the cross-government "Sanctions enforcement action" collection: trimmed toward the ~85 target. Both URLs loaded, and they duplicate other entries.
- Point Source: could not confirm a URL (pointsourceinvestigations.co.uk did not resolve).
- Tortoise and OCCRP: trimmed. Both loaded, and they are optional for the UK list.
- Insolvency Service organisation page, gov.uk organisations list, Tax and Chancery and Administrative Appeals tribunal decision pages, Independent Adviser on Ministerial Standards page and Members API: all loaded but were trimmed as overlapping. They are easy to add back.
- FCA enforcement news page: blocked by Cloudflare (the FCA homepage and the register loaded).

## Unsure
- FIRS public register: we confirmed only the GOV.UK guidance page about what the register publishes, not a stable URL for the searchable register itself. Worth a manual browser check.
- CourtServe and Jersey/Guernsey/IoM access levels ("partly paid") come from general knowledge of their fee models. They were not verified on the pages.
- Electoral Commission £11,180 central reporting threshold (in force since Jan 2024): re-check if thresholds change again.
- Strategic export controls database (exportcontroldb.trade.gov.uk) did not resolve and was not used. The control lists are reachable via gov.uk/guidance/uk-strategic-export-controls.

## Part B: land, environment, maps, military, transport, policing, health, statistics, media, tools

95 entries in 10 categories. All URLs opened one at a time with curl (browser User-Agent, follow redirects, 20 s timeout).

## Moved (status "changed" or new URL used)
- REPD: monthly-extract page redirects to the quarterly extract.
- statistics.gov.scot -> data.gov.scot ("Data about Scotland").
- statswales.gov.wales -> stats.gov.wales/en-GB.
- Nominet: nominet.uk/whois -> nominet.uk/lookup/.
- OS Open Data: ordnancesurvey.co.uk/products/os-open-data is 404; used osdatahub.os.uk/downloads/open.
- G-INFO: siteapps.caa.co.uk/g-info no longer connects; now caa.co.uk/aircraft-register/g-info/search-g-info/.
- Ofcom broadcast bulletins moved under /broadcast-standards/broadcast-bulletins.
- INQUEST deaths-in-custody page 404; used inquest.org.uk/campaigning-for-change/statistics/.
- Police Scotland performance page 404; used /crime-data/.
- Land Registry OCOD/CCOD/INSPIRE: linked to GOV.UK guidance pages, because the download service (use-land-property-data.service.gov.uk) returns 403 to scripts.
- Rivers Trust: linked the map itself (theriverstrust.org/sewage-map).
- Ofcom Wireless Telegraphy Register: no working HTML page found (old /wireless-telegraphy-register path 404); linked the official daily CSV on static.ofcom.org.uk (about 50 MB).
- data.gov.uk dataset pages now carry "National Data Library" branding.

## Unreachable from our checker (kept, marked)
Ofwat (403), NLS maps (human verification), Geograph, Historic England aerial archive, Defence Committee, OpenPrescribing, NHS England Digital, House of Commons Library (all Cloudflare), NHS England statistics and Ofsted reports (202 bot challenge, empty body), Meta Ad Library (403), British Newspaper Archive (security check), crt.sh (502), archive.today (timeout).

## Dropped
- Defence Sourcing Portal (contracts.mod.uk): certificate does not match hostname; replaced by MOD trade, industry and contracts statistics.
- LandWeb Direct (NI): certificate chain error; NI Land & Property Services page later trimmed for length.
- Surfers Against Sewage alerts: Cloudflare, and not on the brief.
- British Library newspapers guide: URLs tried were 404; used British Newspaper Archive instead.
- Defence equipment plan reports: series appears to have stopped years ago; NAO covers it.
- UK Registry of Outer Space Objects: GOV.UK page last updated January 2021; CAA space licences page kept instead.
- UK Ship Register: no public search found.
- Trimmed for length (all worked): Who Owns Scotland, ScotLIS (mentioned in RoS note), NI LPS, Stream water data, EA Water Quality Explorer, NAEI, Britain From Above, Digimap, OS Maps, DE&S, Navy Lookout, UK Defence Journal, VesselFinder (mentioned in MarineTraffic note), Flightradar24, MCA, Fire statistics, Netpol, Public Health Scotland, Internet Archive TV News, TikTok Ad Library, Hunchly, London Datastore.
- Out of scope by rule: people-search, electoral roll, DVLA, sex-offender lookups, Forces War Records.

## Unsure / for the merge
- Register of Overseas Entities, Contracts Finder, Find a Tender, Wayback Machine and Hansard left for part A's categories (companies, spending, archives, parliament); check they are there.
- Planning Portal run_by: "PortalPlanQuest Ltd for MHCLG" from memory of its ownership; verify.
- ADS-B Exchange run_by "owned by Jetnet" and MarineTraffic "Kpler" are from knowledge, not checked today.
- Stat-Xplore guest access note is from knowledge.
