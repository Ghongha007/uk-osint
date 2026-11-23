# UK OSINT

Public records, open data, research databases and tools for investigating stories about the United Kingdom, including Scotland, Wales and Northern Ireland, with pointers to the Crown Dependencies. Every link was checked on the date shown beside it.

**186 sources. Last full check: 2026-11-23.** 156 loaded for us; 30 could not be reached from our checker and are marked in the table. Some official sites block automated checks, so a source marked that way may still work for you in a browser.

## How to read the tables

- **Access** says what stands between you and the data: *Open* (nothing), *Free login*, *Captcha* (free, but a captcha on each search), *Paid*, or *Partly paid*.
- **Run by** tells you whose data it is. A government register, a company, a charity and a newsroom each have different reasons to be right or wrong.
- **Checked** is the date we last opened the link. Registers get rebuilt and moved (procurement moved to a new platform under the Procurement Act 2023), so if the date is old, check the link before relying on it.
- Notes in *italics* are caveats we hit while testing.

## What is deliberately left out

This list covers records about companies, charities, political money, public spending, courts, Parliament, sanctions, land ownership, the environment, the military, transport, policing and public data. It does not include people-search sites, electoral-roll or phone, address and vehicle-owner lookups of private individuals, sex-offender or mugshot lookups, or anything built on breached personal data. Leak databases published by newsrooms are included and marked.

## Using these sources well

- **A record shows what was filed, not what is true.** Companies House does not verify most of what it is sent, though identity checks for directors began in 2025. Treat filings as claims made by the filer.
- **Archive what you find.** Save pages to the Wayback Machine or archive.today and keep a dated copy. Companies House documents can be corrected or removed.
- **Names are not unique.** Match on a second detail (a company number, a charity number, a title number, a date of birth month and year as shown on Companies House) before saying two records are the same person or company.
- **Mind the law.** UK defamation, contempt of court and reporting restrictions are strict, and data protection law applies to what you collect about people. Check before you publish.

## Contents

- [Companies, charities and money](#companies-charities-and-money) (14)
- [Political donations, lobbying and influence](#political-donations-lobbying-and-influence) (11)
- [Public spending, contracts and grants](#public-spending-contracts-and-grants) (11)
- [Courts, tribunals and law](#courts-tribunals-and-law) (14)
- [Parliament, government and officials](#parliament-government-and-officials) (14)
- [Sanctions and export controls](#sanctions-and-export-controls) (9)
- [Land, property and planning](#land-property-and-planning) (10)
- [Environment and energy](#environment-and-energy) (9)
- [Maps, satellite and geodata](#maps-satellite-and-geodata) (9)
- [Military and defence](#military-and-defence) (8)
- [Maritime, aviation and space](#maritime-aviation-and-space) (10)
- [Police, crime and public safety](#police-crime-and-public-safety) (10)
- [Health, education and welfare data](#health-education-and-welfare-data) (10)
- [Statistics and open data](#statistics-and-open-data) (9)
- [Media, social platforms and ad transparency](#media-social-platforms-and-ad-transparency) (8)
- [FOI, documents and archives](#foi-documents-and-archives) (10)
- [Investigative outlets and research groups](#investigative-outlets-and-research-groups) (11)
- [Tools and search techniques](#tools-and-search-techniques) (9)

## Companies, charities and money

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [Charity Commission for Northern Ireland register](https://www.charitycommissionni.org.uk/charity-search/) | Look up Northern Ireland charities with their trustees, finances and annual reports. | Open | Charity Commission for Northern Ireland | 2026-11-23 |
| [Charity Commission register of charities](https://register-of-charities.charitycommission.gov.uk/en/) | Look up charities in England and Wales with their trustees, income and spending, annual accounts, and any regulatory action. *Full accounts are published only for charities with income over £25,000.* | Open | Charity Commission for England and Wales | 2026-11-23 |
| [Companies House API](https://developer.company-information.service.gov.uk/) | Pull company profiles, officers, PSCs, filing histories and charges by script, including searches for every appointment held by an officer. *Needs a free API key; rate limits apply.* | Free login | Companies House (UK government) | 2026-11-23 |
| [Companies House PSC bulk data](https://download.companieshouse.gov.uk/en_pscdata.html) | Download a daily snapshot of the persons with significant control register, the people and firms said to own or control UK companies. *Large JSON files. PSC entries are self-declared and often incomplete or show another company as the controller.* | Open | Companies House (UK government) | 2026-11-23 |
| [Companies House search (Find and update company information)](https://find-and-update.company-information.service.gov.uk/) | Look up any UK company, including those in Northern Ireland, with its officers, persons with significant control (PSCs), filed accounts, charges and full filing history back to the 1980s for many firms. *Information is shown as filed. Companies House began verifying the identities of directors and PSCs in November 2025; older filings were not checked. Use the advanced search to filter by name, location, incorporation date or company type.* | Open | Companies House (UK government) | 2026-11-23 |
| [FCA Financial Services Register](https://register.fca.org.uk/s/) | Check whether a firm or individual is authorised to do financial business in the UK, what they are allowed to do, and any disciplinary history. *The page relies on scripts and can be slow.* | Open | Financial Conduct Authority (FCA) | 2026-11-23 |
| [Guernsey Registry](https://www.greg.gg/) | Search companies, foundations and other entities registered in Guernsey, a Crown Dependency with its own company register. *The site returned a maintenance page to our checker on 23 Nov 2026. Basic searches are free; documents carry fees.* | Partly paid | Guernsey Registry (States of Guernsey) | 2026-11-23 (not reachable from our checker) |
| [Isle of Man Companies Registry](https://services.gov.im/companies-registry) | Search companies registered in the Isle of Man, a Crown Dependency, and order their filed documents. *Searches are free; copies of documents are charged.* | Partly paid | Isle of Man Government | 2026-11-23 |
| [Jersey Financial Services Commission registry](https://www.jerseyfsc.org/registry/registry-entities/) | Search companies, partnerships and other entities registered in Jersey, a Crown Dependency with its own company register. *Basic entity details are free; filed documents may carry a fee. Beneficial ownership details are not publicly searchable.* | Partly paid | Jersey Financial Services Commission | 2026-11-23 |
| [OpenCorporates](https://opencorporates.com/) | Search UK companies alongside registries from 140+ other jurisdictions, useful for following a company or officer across borders, including the Crown Dependencies where covered. *Free to search; bulk data and API are paid except for journalists and NGOs who apply.* | Partly paid | OpenCorporates Ltd (UK, public-benefit company) | 2026-11-23 |
| [OSCR Scottish Charity Register](https://www.oscr.org.uk/about-charities/search-the-register/) | Look up Scottish charities with their purposes, governing documents, income, spending and annual accounts. | Open | Office of the Scottish Charity Regulator (OSCR) | 2026-11-23 |
| [Register of Overseas Entities](https://www.gov.uk/government/collections/register-of-overseas-entities) | Find out how foreign companies that own UK land must declare their beneficial owners; the entities themselves are searchable in the normal Companies House search. *This page is the guidance collection. Information about trusts behind an entity is not public and must be requested from Companies House with a reason.* | Open | Companies House (UK government) | 2026-11-23 |
| [Search for disqualified company directors](https://www.gov.uk/search-the-register-of-disqualified-company-directors) | Check whether someone has been banned from running UK companies, and for how long. | Open | Companies House and the Insolvency Service (UK government) | 2026-11-23 |
| [The Gazette insolvency notices](https://www.thegazette.co.uk/insolvency/notice) | Search official notices of company liquidations, administrations, winding-up petitions and strikings-off, with dates and appointed insolvency practitioners. *The Gazette also prints notices about personal bankruptcies; use the company notices for company stories.* | Open | The Gazette (The Stationery Office for the UK government) | 2026-11-23 |

## Political donations, lobbying and influence

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [Advisory Committee on Business Appointments (ACOBA)](https://www.gov.uk/government/organisations/advisory-committee-on-business-appointments) | Read the advice letters on jobs taken by former ministers and senior civil servants after leaving government, with the conditions attached. *Advice is published only once the appointment is announced or taken up, and ACOBA has no power to block jobs.* | Open | Advisory Committee on Business Appointments | 2026-11-23 |
| [Electoral Commission donations and loans search](https://search.electoralcommission.org.uk/) | Search reported donations and loans to UK political parties, MPs, candidates and campaigners, plus party accounts and election spending returns. *Parties report quarterly; donations to a party under £11,180 are not reported centrally. Northern Ireland donor details are published only from July 2017.* | Open | Electoral Commission | 2026-11-23 |
| [Foreign Influence Registration Scheme: public register guidance](https://www.gov.uk/government/publications/foreign-influence-registration-scheme-registration-and-public-register) | Learn which arrangements to carry out political influence activity for foreign powers are published on the FIRS public register, and what is kept back. *The scheme began on 1 July 2025. We could not confirm a stable link to the searchable register itself, so start from this guidance.* | Open | Home Office (UK government) | 2026-11-23 |
| [List of Ministers' Interests](https://www.gov.uk/government/publications/list-of-ministers-interests) | See the interests ministers have declared under the Ministerial Code, including those of close family that could conflict with their role. *Published only a few times a year.* | Open | Cabinet Office and Independent Adviser on Ministerial Standards | 2026-11-23 |
| [Ministers' transparency publications (Cabinet Office)](https://www.gov.uk/government/collections/ministers-transparency-publications) | Find quarterly lists of ministers' meetings with outside organisations, gifts, hospitality and overseas travel. *Releases are often months late and give only the organisation and a one-word purpose. Other departments publish their own; find them through GOV.UK's transparency search.* | Open | Cabinet Office (UK government) | 2026-11-23 |
| [openDemocracy Dark Money Investigations](https://www.opendemocracy.net/tag/dark-money-investigations/) | Read investigations into undeclared political funding, think-tank money and lobbying in the UK, often with the documents they obtained. | Open | openDemocracy | 2026-11-23 |
| [Register of All-Party Parliamentary Groups](https://www.parliament.uk/mps-lords-and-offices/standards-and-financial-interests/parliamentary-commissioner-for-standards/registers-of-interests/register-of-all-party-party-parliamentary-groups/) | See every all-party parliamentary group, its officers, who runs its secretariat and which companies or charities give it money or help. *Parliament's site sits behind a bot check that blocked our checker; loads in a browser.* | Open | House of Commons (Parliamentary Commissioner for Standards) | 2026-11-23 (not reachable from our checker) |
| [Register of Consultant Lobbyists](https://orcl.my.site.com/CLR_Search) | Search lobbying firms registered in the UK and the clients they declared each quarter. *Covers only third-party lobbyists who contact ministers or permanent secretaries; in-house lobbyists are not on it.* | Open | Office of the Registrar of Consultant Lobbyists (ORCL) | 2026-11-23 |
| [Register of Lords' Interests](https://members.parliament.uk/members/lords/interests/register-of-lords-interests) | See peers' declared directorships, paid work, shareholdings, gifts and visits. *Parliament's site sits behind a bot check that blocked our checker; loads in a browser.* | Open | House of Lords (Lords Commissioner for Standards) | 2026-11-23 (not reachable from our checker) |
| [Register of Members' Financial Interests (House of Commons)](https://www.parliament.uk/mps-lords-and-offices/standards-and-financial-interests/parliamentary-commissioner-for-standards/registers-of-interests/register-of-members-financial-interests/) | See MPs' declared second jobs, gifts, overseas trips, donations, shareholdings and property. *Parliament's site sits behind a bot check that blocked our checker; loads in a browser. The same register is available as data from the Register of Interests API (interests-api.parliament.uk).* | Open | House of Commons (Parliamentary Commissioner for Standards) | 2026-11-23 (not reachable from our checker) |
| [Transparency International UK](https://www.transparency.org.uk/) | Read research on UK lobbying, political donations, revolving doors and dirty money in UK property, plus its open-data tools on influence. *A bot check blocked our checker; loads in a browser.* | Open | Transparency International UK (charity) | 2026-11-23 (not reachable from our checker) |

## Public spending, contracts and grants

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [360Giving GrantNav](https://grantnav.threesixtygiving.org/) | Search grants made by UK funders, including government departments, the National Lottery and charitable foundations, with recipients and amounts. *Rate-limited our checker; the 360Giving site (360giving.org) loaded. Only funders who publish to the 360Giving standard are included.* | Open | 360Giving (charity) | 2026-11-23 (not reachable from our checker) |
| [Contracts Finder](https://www.contractsfinder.service.gov.uk/Search) | Search public contracts and awards in England from 2015 onwards, including many lower-value contracts with supplier names and values. *Procurements started under the Procurement Act 2023 (from 24 Feb 2025) are published on Find a Tender instead, so recent coverage is mostly legacy contracts.* | Open | Cabinet Office (UK government) | 2026-11-23 |
| [Find a Tender (Central Digital Platform)](https://www.find-tender.service.gov.uk/Search) | Search UK public procurement notices, from tenders to contract awards and changes; since February 2025 this is the central platform for notices under the Procurement Act 2023. *Covers notices from 2021; earlier high-value notices were in the EU's TED.* | Open | Cabinet Office (UK government) | 2026-11-23 |
| [Good Law Project](https://goodlawproject.org/) | Read legal challenges and reporting on pandemic contracts, including the 'VIP lane' for PPE suppliers. *A bot check blocked our checker; loads in a browser. It is a campaigning organisation, so check its claims against the court judgments and NAO reports.* | Open | Good Law Project (campaign group) | 2026-11-23 (not reachable from our checker) |
| [GOV.UK transparency releases: spending over £25,000](https://www.gov.uk/search/transparency-and-freedom-of-information-releases?keywords=spending+over+25000) | Find each department's monthly list of individual payments over £25,000, with supplier, amount and spending area. *Every department publishes its own spreadsheets in slightly different formats, often late.* | Open | UK government departments (via GOV.UK) | 2026-11-23 |
| [Local government transparency code](https://www.gov.uk/government/publications/local-government-transparency-code-2015) | Learn what English councils must publish, including every payment over £500, contracts over £5,000 and senior salaries, then find the data on each council's own site. *There is no single national database of council spending; quality varies by council.* | Open | Ministry of Housing, Communities and Local Government (UK government) | 2026-11-23 |
| [National Audit Office](https://www.nao.org.uk/) | Read the independent auditor's reports on how government spends money, with value-for-money studies of major projects, contracts and departments. | Open | National Audit Office (NAO) | 2026-11-23 |
| [Open Opportunities (Spend Network)](https://openopps.com/) | Search tender and contract notices gathered from the UK and many other countries in one place. *Limited free search; full access is paid.* | Partly paid | Spend Network Ltd | 2026-11-23 |
| [Procurement Act 2023 guidance](https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents) | Understand the notices public bodies must now publish under the Procurement Act 2023, such as contract details, payments and performance reports. | Open | Cabinet Office (UK government) | 2026-11-23 |
| [Public Accounts Committee](https://committees.parliament.uk/committee/127/public-accounts-committee/) | Read reports and evidence from the Commons committee that questions officials about government waste and failing projects, often building on NAO work. *Parliament's site sits behind a bot check that blocked our checker; loads in a browser.* | Open | House of Commons | 2026-11-23 (not reachable from our checker) |
| [Tussell](https://www.tussell.com/) | Analyse UK public sector contracts and spending by supplier, buyer and framework, with cleaned data across central and local government. | Paid | Tussell Ltd | 2026-11-23 |

## Courts, tribunals and law

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [BAILII](https://www.bailii.org/) | Search a large free collection of judgments from courts across the UK and Ireland, including older and Scottish and Northern Irish cases. *A bot check blocked our checker; loads in a browser.* | Open | British and Irish Legal Information Institute (charity) | 2026-11-23 (not reachable from our checker) |
| [Court and tribunal hearings](https://www.court-tribunal-hearings.service.gov.uk/) | View daily hearing lists for courts and tribunals in England and Wales, to find when a case is in court. *Some lists, such as detailed magistrates' court registers, are available only to verified media users who sign in.* | Open | HM Courts and Tribunals Service (HMCTS) | 2026-11-23 |
| [Courts and Tribunals Judiciary judgments](https://www.judiciary.uk/judgments/) | Read selected judgments and sentencing remarks from high-profile cases in England and Wales. | Open | Courts and Tribunals Judiciary | 2026-11-23 |
| [CourtServe](https://www.courtserve.net/) | Check court lists for England and Wales in one place, including magistrates' and Crown court lists. *Some lists are free; fuller access is a subscription.* | Partly paid | CourtServe Ltd | 2026-11-23 |
| [CPS News Centre](https://www.cps.gov.uk/news) | Find charging decisions and convictions announced by the Crown Prosecution Service in England and Wales. | Open | Crown Prosecution Service (CPS) | 2026-11-23 |
| [Employment tribunal decisions](https://www.gov.uk/employment-tribunal-decisions) | Search employment tribunal judgments in England, Wales and Scotland, useful for workplace stories about named employers. *Decisions are published from February 2017 onwards.* | Open | HM Courts and Tribunals Service (via GOV.UK) | 2026-11-23 |
| [Find Case Law](https://caselaw.nationalarchives.gov.uk/) | Search judgments and tribunal decisions from courts in England and Wales and UK-wide courts, mostly from 2001 onwards, as free official copies. | Open | The National Archives | 2026-11-23 |
| [Judiciary NI judicial decisions](https://www.judiciaryni.uk/judicial-decisions) | Read judgments and sentencing remarks from Northern Ireland's courts. | Open | Judiciary NI | 2026-11-23 |
| [legislation.gov.uk](https://www.legislation.gov.uk/) | Read UK Acts and statutory instruments as passed and as currently in force, including Scottish, Welsh and Northern Ireland law. *Returned an empty bot-protection response to our checker; loads in a browser.* | Open | The National Archives | 2026-11-23 (not reachable from our checker) |
| [Prevention of future deaths reports](https://www.judiciary.uk/prevention-of-future-death-reports/) | Read coroners' warnings to organisations after inquests found risks of further deaths, with the responses they received. *Covers England and Wales only.* | Open | Courts and Tribunals Judiciary (Chief Coroner) | 2026-11-23 |
| [Scottish Courts and Tribunals judgments](https://www.scotcourts.gov.uk/judgments/) | Search judgments from Scotland's Court of Session, High Court of Justiciary, sheriff courts and tribunals. | Open | Scottish Courts and Tribunals Service | 2026-11-23 |
| [Serious Fraud Office](https://www.gov.uk/government/organisations/serious-fraud-office) | Follow fraud, bribery and corruption cases, charges, deferred prosecution agreements and outcomes brought by the SFO. *The SFO now publishes on GOV.UK; the old sfo.gov.uk address did not respond.* | Open | Serious Fraud Office (UK government) | 2026-11-23 |
| [UK Supreme Court cases](https://www.supremecourt.uk/cases?cs=Judgment+given&p=1) | Follow cases at the UK's highest court, with judgments, press summaries and video of hearings. | Open | The Supreme Court of the United Kingdom | 2026-11-23 |
| [Upper Tribunal (Immigration and Asylum Chamber) decisions](https://tribunalsdecisions.service.gov.uk/utiac) | Search immigration and asylum appeal decisions from the Upper Tribunal, including reported country guidance cases. | Open | HM Courts and Tribunals Service | 2026-11-23 |

## Parliament, government and officials

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [Civil Service statistics](https://www.gov.uk/government/collections/civil-service-statistics) | Find annual figures on the size, pay and make-up of the civil service by department, grade and location. *Names and salaries of senior officials appear in each department's organisation chart releases, found via GOV.UK's transparency search.* | Open | Cabinet Office (UK government) | 2026-11-23 |
| [GOV.UK search](https://www.gov.uk/search/all) | Search every policy paper, statistic, transparency release, FOI release and news story published by UK government departments and agencies. *GOV.UK also has a public search API at gov.uk/api/search.json.* | Open | Government Digital Service (UK government) | 2026-11-23 |
| [Hansard](https://hansard.parliament.uk/) | Search the official record of everything said in the Commons and Lords, including debates, statements and division votes. *Parliament's site sits behind a bot check that blocked our checker; loads in a browser.* | Open | UK Parliament | 2026-11-23 (not reachable from our checker) |
| [IPSA MPs' staffing and business costs](https://www.theipsa.org.uk/mp-staffing-business-costs) | See what each MP claimed for offices, staff, travel and accommodation, claim by claim. *Published in batches, usually a few months behind.* | Open | Independent Parliamentary Standards Authority (IPSA) | 2026-11-23 |
| [Members' Names Data Platform](https://data.parliament.uk/membersdataplatform/) | Get structured data on every MP and peer, past and present, with constituencies, parties, posts held and dates. *The newer Members API (members-api.parliament.uk) carries much of the same data.* | Open | UK Parliament | 2026-11-23 |
| [Ministerial Code](https://www.gov.uk/government/publications/ministerial-code) | Read the rules ministers must follow on conflicts of interest, gifts and conduct, to measure a story against. | Open | Cabinet Office (UK government) | 2026-11-23 |
| [Northern Ireland Assembly](https://www.niassembly.gov.uk/) | Search Hansard, questions, committees and Members' register of interests for the Northern Ireland Assembly. | Open | Northern Ireland Assembly | 2026-11-23 |
| [Parliament bills](https://bills.parliament.uk/) | Track every bill before Parliament with its stages, amendments, votes and published versions. *Blocked our checker; loads in a browser. Also available as data through the Bills API (bills-api.parliament.uk).* | Open | UK Parliament | 2026-11-23 (not reachable from our checker) |
| [Parliament committees](https://committees.parliament.uk/) | Read select committee inquiries, reports, written evidence and transcripts of oral evidence sessions. *Blocked our checker; loads in a browser. The Committees API (committees-api.parliament.uk) loaded.* | Open | UK Parliament | 2026-11-23 (not reachable from our checker) |
| [Scottish Parliament](https://www.parliament.scot/) | Search the Official Report, bills, committees, written questions and MSPs' register of interests for the Scottish Parliament. | Open | Scottish Parliament | 2026-11-23 |
| [Senedd Cymru](https://senedd.wales/) | Search the Record of Proceedings, committees, laws and Members' register of interests for the Welsh Parliament. | Open | Senedd Cymru (Welsh Parliament) | 2026-11-23 |
| [TheyWorkForYou](https://www.theyworkforyou.com/) | Follow what an MP or peer has said, how they voted and what they declared, with email alerts on any word in Hansard. *Returned rate-limit and error pages to our checker on 23 Nov 2026.* | Open | mySociety (charity) | 2026-11-23 (not reachable from our checker) |
| [Who's Who](https://www.ukwhoswho.com/) | Read self-written biographies of prominent people in British public life, including career, education and clubs, back to 1897 in Who Was Who. *Entries are written by the subjects themselves. Many UK public libraries give free access with a library card.* | Paid | Oxford University Press | 2026-11-23 |
| [Written questions, answers and statements](https://questions-statements.parliament.uk/) | Search MPs' and peers' written questions with ministers' answers, and written ministerial statements, a rich source of official figures. *Blocked our checker; loads in a browser. The API at questions-statements-api.parliament.uk loaded.* | Open | UK Parliament | 2026-11-23 (not reachable from our checker) |

## Sanctions and export controls

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [CAAT UK arms export data](https://caat.org.uk/data/exports-uk/) | Browse UK arms export licences by country and equipment type in an easier format than the official statistics. *Built from the official licensing statistics by a campaign group.* | Open | Campaign Against Arms Trade (campaign group) | 2026-11-23 |
| [Notices to exporters (incl. compound settlements)](https://www.gov.uk/government/collections/notices-to-exporters) | Read official notices on export control changes and HMRC compound settlements, the fines paid by firms that broke export rules. *Most compound settlement notices do not name the company.* | Open | Department for Business and Trade and HM Revenue and Customs | 2026-11-23 |
| [OFSI Consolidated List search (archived)](https://sanctionssearchapp.ofsi.hmtreasury.gov.uk/) | Search the former Treasury list of asset-freeze targets as it stood up to 28 January 2026. *Closed on 28 January 2026 and no longer updated; use the UK Sanctions List for current designations.* | Open | Office of Financial Sanctions Implementation (HM Treasury) | 2026-11-23 |
| [OFSI financial sanctions enforcement and penalties](https://www.gov.uk/government/collections/enforcement-of-financial-sanctions) | Read the penalty notices and disclosures naming firms and people that breached UK financial sanctions, with the amounts involved. | Open | Office of Financial Sanctions Implementation (HM Treasury) | 2026-11-23 |
| [OpenSanctions](https://www.opensanctions.org/) | Search UK sanctions together with other countries' lists, politically exposed persons and watchlists in one database. *Free for non-commercial use; commercial use needs a licence.* | Partly paid | OpenSanctions Datenbanken GmbH | 2026-11-23 |
| [OTSI trade sanctions civil enforcement](https://www.gov.uk/government/collections/trade-sanctions-civil-enforcement) | Read penalty notices from the office that enforces UK trade sanctions on goods and services. | Open | Office of Trade Sanctions Implementation (Department for Business and Trade) | 2026-11-23 |
| [Strategic export controls: licensing statistics](https://www.gov.uk/guidance/strategic-export-controls-licensing-statistics) | Find quarterly and annual data on UK export licences for arms and dual-use goods, by destination, goods type and decision. *Shows licence types and rating categories, not named exporters or deal values for most licences.* | Open | Export Control Joint Unit (Department for Business and Trade) | 2026-11-23 |
| [The UK Sanctions List (downloads)](https://www.gov.uk/government/publications/the-uk-sanctions-list) | Download the full UK Sanctions List as data files to match against company or shipping records. | Open | Foreign, Commonwealth and Development Office (FCDO) | 2026-11-23 |
| [UK Sanctions List search](https://search-uk-sanctions-list.service.gov.uk/) | Search every person, company and ship under UK sanctions, with the reasons, aliases and dates of designation. *Since 28 January 2026 this is the single official list of UK sanctions designations.* | Open | Foreign, Commonwealth and Development Office (FCDO) | 2026-11-23 |

## Land, property and planning

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [HM Land Registry title search](https://www.gov.uk/search-property-information-land-registry) | Buy the title register and title plan for any registered property in England and Wales, showing the owner, price paid (where recorded), mortgages and restrictions. *Searching is free; each title register or plan costs a small fee. About 13% of land in England and Wales is still unregistered.* | Partly paid | HM Land Registry | 2026-11-23 |
| [INSPIRE Index Polygons](https://www.gov.uk/guidance/inspire-index-polygons-spatial-data) | Download the boundary shapes of freehold registered land in England and Wales, council by council, to see where one title ends and the next begins. *Polygons carry an ID, not the owner: you still need the title number from the register or OCOD/CCOD to link them.* | Free login | HM Land Registry | 2026-11-23 |
| [Overseas companies that own property in England and Wales (OCOD)](https://www.gov.uk/guidance/hm-land-registry-overseas-companies-that-own-property-in-england-and-wales) | Download every registered title in England and Wales owned by a company incorporated abroad, with the company name, jurisdiction, address and price paid. *Download sits on the Use land and property data service, which blocked our script (403) but works in a browser after a free account. Match owners against the Register of Overseas Entities at Companies House.* | Free login | HM Land Registry | 2026-11-23 |
| [Planning Portal](https://www.planningportal.co.uk/) | Find which council handles planning in England and Wales and follow links to its online planning application search. *Applications themselves sit on each council's own search, with different systems and retention periods.* | Open | PortalPlanQuest Ltd for the Ministry of Housing, Communities and Local Government | 2026-11-23 |
| [Price Paid Data](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads) | Download every residential property sale in England and Wales since 1995, with price, date, address and property type. *Covers sales at full market value only; many company and bulk transactions are missing. A search interface is at landregistry.data.gov.uk/app/ppd.* | Open | HM Land Registry | 2026-11-23 |
| [Register of Persons Holding a Controlled Interest in Land (RCI)](https://www.ros.gov.uk/our-registers/register-of-persons-holding-a-controlled-interest-in-land) | Find the people who actually control land in Scotland held through trusts, overseas entities, partnerships and other opaque owners. *In force since April 2024; filings depend on owners complying.* | Open | Registers of Scotland | 2026-11-23 |
| [Registers of Scotland](https://www.ros.gov.uk/) | Buy title sheets and search Scotland's land and property registers, including the Land Register and the Sasine Register. *Map search and last price paid are free on ScotLIS (scotlis.ros.gov.uk); title sheets cost a fee.* | Partly paid | Registers of Scotland | 2026-11-23 |
| [UK companies that own property in England and Wales (CCOD)](https://www.gov.uk/guidance/hm-land-registry-uk-companies-that-own-property-in-england-and-wales) | Download every registered title owned by a UK-registered company or corporate body, with its company number, so you can map a firm's whole property portfolio. *Same free-account download service as OCOD. Individuals' holdings are not included.* | Free login | HM Land Registry | 2026-11-23 |
| [Valuation Office Agency business rates search](https://www.tax.service.gov.uk/business-rates-find/search) | Look up the rateable value, floor areas and valuation details of any shop, office, warehouse or other non-domestic property in England and Wales. *Shows the property, not who occupies or owns it.* | Open | Valuation Office Agency (HMRC) | 2026-11-23 |
| [Who Owns England?](https://whoownsengland.org/) | Read investigations and maps of who owns England's land, from aristocratic estates and the Crown to offshore companies and public bodies. *Campaigning project; maps are built from Land Registry and other datasets and may lag behind them.* | Open | Guy Shrubsole and Anna Powell-Smith (independent project) | 2026-11-23 |

## Environment and energy

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [Defra Data Services Platform](https://environment.data.gov.uk/) | Find and download Defra and Environment Agency datasets on flooding, pollution, land, water and wildlife, many as maps or APIs. | Open | Department for Environment, Food and Rural Affairs (Defra) | 2026-11-23 |
| [DESNZ energy statistics](https://www.gov.uk/government/organisations/department-for-energy-security-and-net-zero/about/statistics) | Get official UK figures on energy production, prices, fuel poverty, emissions and the Digest of UK Energy Statistics (DUKES). | Open | Department for Energy Security and Net Zero (DESNZ) | 2026-11-23 |
| [Environment Agency public registers](https://environment.data.gov.uk/public-register/view/index) | Search environmental permits, waste carriers, enforcement actions and water discharge consents in England by company, site or postcode. | Open | Environment Agency | 2026-11-23 |
| [Event Duration Monitoring: storm overflow annual returns](https://www.data.gov.uk/dataset/19f6064d-7356-466f-844e-d20ea10ae9fd/storm-overflow-annual-returns) | Download how many times and for how many hours each water company storm overflow in England spilled sewage, year by year. *Self-reported by water companies; monitors can be faulty or offline, which the files flag.* | Open | Environment Agency | 2026-11-23 |
| [Ofgem](https://www.ofgem.gov.uk/) | Find energy supplier licences, enforcement decisions, fines, price cap data and network company performance. | Open | Office of Gas and Electricity Markets (Ofgem) | 2026-11-23 |
| [Ofwat](https://www.ofwat.gov.uk/) | Read water company performance reports, enforcement cases, fines and price review decisions for England and Wales. *Our script got a 403 error page; loads in a browser.* | Open | Water Services Regulation Authority (Ofwat) | 2026-11-23 (not reachable from our checker) |
| [Renewable Energy Planning Database (REPD)](https://www.gov.uk/government/publications/renewable-energy-planning-database-quarterly-extract) | Track every wind, solar, battery and other renewable project above 150kW through planning, from application to refusal or operation, with developer and location. *Old monthly-extract address now redirects here; the file is published quarterly.* | Open | Department for Energy Security and Net Zero (DESNZ) | 2026-11-23 |
| [Rivers Trust Sewage Map](https://theriverstrust.org/sewage-map) | See every storm overflow in England and Wales on a map, with spill counts and hours, and the rivers and beaches downstream. *Built from official event duration monitoring data, so it carries the same gaps.* | Open | The Rivers Trust | 2026-11-23 |
| [SEPA](https://www.sepa.org.uk/) | Find Scottish environmental licences, enforcement action, pollution inventories and water quality data. | Open | Scottish Environment Protection Agency (SEPA) | 2026-11-23 |

## Maps, satellite and geodata

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [Copernicus Browser](https://browser.dataspace.copernicus.eu/) | View and download free Sentinel satellite images of any part of the UK, often every few days, to see change on the ground. *Sentinel-2 resolution is 10 metres: good for fires, floods and land clearance, not vehicles.* | Free login | European Space Agency (ESA) / European Commission | 2026-11-23 |
| [Defra Survey Data Download (LIDAR)](https://environment.data.gov.uk/survey) | Download Environment Agency LIDAR height data and aerial imagery for England, detailed enough to reveal earthworks, quarries and hidden structures. | Open | Environment Agency | 2026-11-23 |
| [Geograph Britain and Ireland](https://www.geograph.org.uk/) | Find millions of geotagged, dated photographs of almost every square kilometre of Britain and Ireland. *Cloudflare check blocked our script; loads in a browser.* | Open | Geograph Project Ltd (charity) | 2026-11-23 (not reachable from our checker) |
| [Google Earth Pro](https://www.google.com/earth/about/versions/) | Use the desktop version of Google Earth to scroll back through historical satellite imagery and measure distances and areas. *Image dates and quality vary by place.* | Open | Google | 2026-11-23 |
| [Historic England aerial photo archive](https://historicengland.org.uk/images-books/archive/collections/aerial-photos/) | Search millions of aerial photographs of England from 1919 onwards, including RAF wartime and post-war cover. *Cloudflare check blocked our script; loads in a browser.* | Open | Historic England | 2026-11-23 (not reachable from our checker) |
| [MAGIC map](https://magic.defra.gov.uk/) | Map protected sites, habitats, flood zones, green belt, ancient woodland and farming schemes across England. | Open | Department for Environment, Food and Rural Affairs (Defra) | 2026-11-23 |
| [National Library of Scotland historic maps](https://maps.nls.uk/) | Compare historic Ordnance Survey maps of the whole UK back to the 1840s, with side-by-side and overlay views against today's maps. *A human-verification check blocked our script; loads in a browser.* | Open | National Library of Scotland | 2026-11-23 (not reachable from our checker) |
| [OS Open Data downloads](https://osdatahub.os.uk/downloads/open) | Download free Ordnance Survey maps and data, including OS OpenMap, boundaries, roads, rivers and building footprints. *The old product page at ordnancesurvey.co.uk/products/os-open-data now returns 404.* | Open | Ordnance Survey | 2026-11-23 |
| [Overpass Turbo](https://overpass-turbo.eu/) | Query OpenStreetMap for every mapped feature of a type in an area, such as all CCTV cameras, military sites or petrol stations. *Results are only as complete as volunteer mapping.* | Open | Martin Raifer (open source), using OpenStreetMap data | 2026-11-23 |

## Military and defence

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [Campaign Against Arms Trade (CAAT)](https://caat.org.uk/) | Use CAAT's research and data on UK arms exports, export licences and arms companies. *Campaign group; its data is built from official licensing records.* | Open | Campaign Against Arms Trade | 2026-11-23 |
| [Drone Wars UK](https://dronewars.net/) | Read research on UK military drones, autonomous weapons and their use, much of it based on FOI requests. *Campaign group.* | Open | Drone Wars UK | 2026-11-23 |
| [House of Commons Defence Committee](https://committees.parliament.uk/committee/24/defence-committee/) | Read MPs' inquiry reports, published evidence and government replies on defence policy, procurement and the armed forces. *Cloudflare check blocked our script; loads in a browser.* | Open | UK Parliament | 2026-11-23 (not reachable from our checker) |
| [MOD official statistics](https://www.gov.uk/government/organisations/ministry-of-defence/about/statistics) | Get official figures on armed forces numbers, recruitment, deaths, injuries, compensation claims, the defence estate and spending. | Open | Ministry of Defence (MOD) | 2026-11-23 |
| [MOD trade, industry and contracts statistics](https://www.gov.uk/government/collections/defence-trade-and-industry-index) | See how much the MOD pays each of its biggest suppliers every year and the value of new contracts, by company and region. *Annual and aggregated; individual contract notices are on Contracts Finder and Find a Tender.* | Open | Ministry of Defence (MOD) | 2026-11-23 |
| [Nuclear Information Service](https://www.nuclearinfo.org/) | Read research on the UK nuclear weapons programme, from Aldermaston and Burghfield to warhead convoys and safety incidents. *Independent research group.* | Open | Nuclear Information Service | 2026-11-23 |
| [Royal Navy equipment pages](https://www.royalnavy.mod.uk/equipment) | See the Royal Navy's ships, submarines and aircraft by class, with names and roles. *Official presentation; check availability and refit status against independent sources.* | Open | Royal Navy (MOD) | 2026-11-23 |
| [Strategic Defence Review 2025](https://www.gov.uk/government/publications/the-strategic-defence-review-2025-making-britain-safer-secure-at-home-strong-abroad) | Read the UK's 2025 defence review, its recommendations on forces, nuclear, industry and procurement, and the government's response. | Open | Ministry of Defence (MOD) | 2026-11-23 |

## Maritime, aviation and space

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [AAIB reports](https://www.gov.uk/aaib-reports) | Search every UK air accident and serious incident investigation report, from airliners to drones and gliders. | Open | Air Accidents Investigation Branch (AAIB) | 2026-11-23 |
| [ADS-B Exchange](https://globe.adsbexchange.com/) | Track aircraft live, including many military and government flights that other trackers filter out, and replay past flights. *Coverage depends on volunteer receivers; historical bulk data is paid.* | Open | ADS-B Exchange (owned by Jetnet) | 2026-11-23 |
| [CAA space licences and permissions](https://www.caa.co.uk/space/licences-and-permissions/) | Find how the UK licenses satellites, launches and spaceports, with lists of licences issued. | Open | UK Civil Aviation Authority (CAA) | 2026-11-23 |
| [Equasis](https://www.equasis.org/EquasisWeb/public/HomePage) | Look up any merchant ship by IMO number to see its owner, manager, flag history, inspections and detentions. *Ownership is often a shell company; follow it through company registries.* | Free login | French Ministry of Transport with the EU and other maritime authorities | 2026-11-23 |
| [G-INFO aircraft register](https://www.caa.co.uk/aircraft-register/g-info/search-g-info/) | Look up any UK-registered aircraft by registration, see its type, registered owner or operator and registration history. *The old siteapps.caa.co.uk/g-info address no longer connects.* | Open | UK Civil Aviation Authority (CAA) | 2026-11-23 |
| [Lloyd's List](https://www.lloydslist.com/) | Read shipping news and investigations on sanctions evasion, dark fleets and ship ownership. *A few articles free each month.* | Paid | Lloyd's List Intelligence (Maritime Intelligence) | 2026-11-23 |
| [MAIB reports](https://www.gov.uk/maib-reports) | Search UK marine accident investigation reports on ships, fishing boats and leisure craft. | Open | Marine Accident Investigation Branch (MAIB) | 2026-11-23 |
| [MarineTraffic](https://www.marinetraffic.com/) | Track ships live by AIS and see recent port calls and positions. *History beyond a short window is paid. Ships can switch AIS off or spoof positions; VesselFinder is a similar alternative.* | Partly paid | Kpler | 2026-11-23 |
| [NATS UK Aeronautical Information Publication (AIP)](https://nats-uk.ead-it.com/cms-nats/opencms/en/Publications/AIP/) | Read the official UK airspace manual, with aerodrome charts, restricted and danger areas and temporary airspace changes. *Live NOTAMs need a separate free registration.* | Open | NATS | 2026-11-23 |
| [Ofcom Wireless Telegraphy Register](https://static.ofcom.org.uk/static/radiolicensing/html/register/WTR.csv) | Download Ofcom's register of radio spectrum licences, showing which companies hold licences for which frequencies and transmitter locations. *A large CSV file (about 50MB), updated daily. Personal licences such as amateur radio are excluded.* | Open | Office of Communications (Ofcom) | 2026-11-23 |

## Police, crime and public safety

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [data.police.uk](https://data.police.uk/) | Download street-level crime, outcomes and stop and search records for every police force in England, Wales and Northern Ireland, with an API. *Locations are snapped to nearby points to protect privacy.* | Open | Home Office | 2026-11-23 |
| [HMICFRS inspection reports](https://hmicfrs.justiceinspectorates.gov.uk/) | Read inspections grading each police force and fire service in England and Wales, plus thematic reports on issues like vetting and custody. | Open | His Majesty's Inspectorate of Constabulary and Fire & Rescue Services | 2026-11-23 |
| [Immigration system statistics](https://www.gov.uk/government/collections/immigration-statistics-quarterly-release) | Get quarterly figures on visas, asylum, small boat arrivals, detention and removals. | Open | Home Office | 2026-11-23 |
| [INQUEST statistics](https://inquest.org.uk/campaigning-for-change/statistics/) | Find counts of deaths in police custody, prisons and mental health detention in England and Wales. *Charity figures can differ from official ones because definitions differ.* | Open | INQUEST (charity) | 2026-11-23 |
| [IOPC](https://www.policeconduct.gov.uk/) | Read investigation reports, recommendations and complaint statistics on police misconduct, deaths and serious injuries in England and Wales. | Open | Independent Office for Police Conduct (IOPC) | 2026-11-23 |
| [ONS crime and justice](https://www.ons.gov.uk/peoplepopulationandcommunity/crimeandjustice) | Get the Crime Survey for England and Wales and police-recorded crime figures, by offence and area. *Survey and police-recorded figures measure different things; police-recorded crime lacks accredited status for some offences.* | Open | Office for National Statistics (ONS) | 2026-11-23 |
| [Police powers and procedures statistics](https://www.gov.uk/government/collections/police-powers-and-procedures-england-and-wales) | Get national figures on arrests, stop and search, detentions, use of force and the outcomes, broken down by force and ethnicity. | Open | Home Office | 2026-11-23 |
| [Police Scotland crime data](https://www.scotland.police.uk/about-us/how-we-do-it/crime-data/) | Get Police Scotland's management information on recorded crime and detection rates by area. *Official crime statistics for Scotland are published separately by the Scottish Government.* | Open | Police Scotland | 2026-11-23 |
| [Police workforce statistics](https://www.gov.uk/government/collections/police-workforce-england-and-wales) | Get officer, staff and PCSO numbers by force, with diversity, joiners, leavers and specialist roles. | Open | Home Office | 2026-11-23 |
| [PSNI official statistics](https://www.psni.police.uk/about-us/our-publications-and-reports/official-statistics) | Get recorded crime, security situation, stop and search and other statistics for Northern Ireland. | Open | Police Service of Northern Ireland (PSNI) | 2026-11-23 |

## Health, education and welfare data

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [CQC](https://www.cqc.org.uk/) | Read inspection reports and ratings for every hospital, care home, GP surgery and dentist in England, with enforcement action. | Open | Care Quality Commission (CQC) | 2026-11-23 |
| [DWP Stat-Xplore](https://stat-xplore.dwp.gov.uk/webapi/jsf/login.xhtml) | Build custom tables of benefit claimants, Universal Credit, sanctions and Personal Independence Payment by area. *Guest access is available without an account for most tables.* | Free login | Department for Work and Pensions (DWP) | 2026-11-23 |
| [Explore education statistics](https://explore-education-statistics.service.gov.uk/) | Build tables from official data on school exclusions, attendance, results, special needs and school funding. | Open | Department for Education | 2026-11-23 |
| [Fingertips public health profiles](https://fingertips.phe.org.uk/) | Compare local areas on hundreds of public health indicators, from life expectancy and obesity to drug deaths. | Open | Office for Health Improvement and Disparities (OHID) | 2026-11-23 |
| [Food hygiene ratings](https://ratings.food.gov.uk/) | Look up the hygiene rating and inspection date of any restaurant, takeaway, shop or food business in England, Wales and Northern Ireland. *Scotland uses a separate pass/improvement scheme on the same site.* | Open | Food Standards Agency | 2026-11-23 |
| [Get Information about Schools](https://get-information-schools.service.gov.uk/) | Look up every school, academy trust and college in England, with its type, governors, trust links and history. | Open | Department for Education | 2026-11-23 |
| [NHS England Digital data and information](https://digital.nhs.uk/data-and-information) | Find NHS datasets such as hospital episode statistics, GP workforce, mental health and prescribing data. *Cloudflare check blocked our script; loads in a browser.* | Open | NHS England | 2026-11-23 (not reachable from our checker) |
| [NHS England statistics](https://www.england.nhs.uk/statistics/) | Get monthly figures on A&E waits, ambulance response times, cancer waits, referral to treatment, beds and more, by hospital trust. *A bot check blocked our script; loads in a browser.* | Open | NHS England | 2026-11-23 (not reachable from our checker) |
| [Ofsted reports](https://reports.ofsted.gov.uk/) | Read inspection reports for schools, nurseries, children's homes and children's services in England. *A bot check blocked our script; loads in a browser.* | Open | Ofsted | 2026-11-23 (not reachable from our checker) |
| [OpenPrescribing](https://openprescribing.net/) | Explore what every GP practice in England prescribes and what it costs, month by month. *Cloudflare check blocked our script; loads in a browser.* | Open | Bennett Institute for Applied Data Science, University of Oxford | 2026-11-23 (not reachable from our checker) |

## Statistics and open data

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [Bank of England Database](https://www.bankofengland.co.uk/boeapps/database/) | Download interest rates, exchange rates, lending, money supply and banking statistics as time series. | Open | Bank of England | 2026-11-23 |
| [Data about Scotland](https://data.gov.scot/) | Find Scottish Government official statistics and open data on population, health, justice and economy. *statistics.gov.scot now redirects here.* | Open | Scottish Government | 2026-11-23 |
| [data.gov.uk](https://www.data.gov.uk/) | Search thousands of datasets published by UK government departments, councils and public bodies. *Now branded National Data Library on dataset pages. Many entries just link to the publisher's site, and some links are dead.* | Open | Department for Science, Innovation and Technology | 2026-11-23 |
| [House of Commons Library](https://commonslibrary.parliament.uk/) | Read impartial research briefings on almost any policy area, with data and links to the official sources. *Cloudflare check blocked our script; loads in a browser.* | Open | UK Parliament | 2026-11-23 (not reachable from our checker) |
| [NISRA](https://www.nisra.gov.uk/) | Get Northern Ireland official statistics, including census, deaths and economic data. | Open | Northern Ireland Statistics and Research Agency (NISRA) | 2026-11-23 |
| [Nomis](https://www.nomisweb.co.uk/) | Build tables of census, jobs, unemployment and benefit data down to small local areas. | Open | Durham University for ONS | 2026-11-23 |
| [Office for National Statistics (ONS)](https://www.ons.gov.uk/) | Get the UK's official statistics on population, economy, jobs, prices, deaths and the census. | Open | Office for National Statistics (ONS) | 2026-11-23 |
| [StatsWales](https://stats.gov.wales/en-GB) | Build tables of Welsh official statistics on health, housing, education, local government and more. *statswales.gov.wales now redirects to this new address.* | Open | Welsh Government | 2026-11-23 |
| [uktradeinfo](https://www.uktradeinfo.com/) | Get official UK import and export figures by product code, country and month, plus lists of registered traders. | Open | HM Revenue & Customs (HMRC) | 2026-11-23 |

## Media, social platforms and ad transparency

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [ASA rulings](https://www.asa.org.uk/codes-and-rulings/rulings.html) | Search rulings on misleading or harmful UK adverts, naming the company and what it was told to change. | Open | Advertising Standards Authority (ASA) | 2026-11-23 |
| [BBC Monitoring](https://monitoring.bbc.co.uk/) | Read translated summaries of foreign broadcasts, press and social media from around the world. | Paid | BBC | 2026-11-23 |
| [Box of Broadcasts](https://learningonscreen.ac.uk/ondemand) | Search and watch recordings of UK TV and radio programmes going back years, with transcripts. *Only for staff and students at subscribing UK universities and colleges.* | Paid | Learning on Screen | 2026-11-23 |
| [Google Ads Transparency Center](https://adstransparency.google.com/) | See ads run by any advertiser on Google Search, YouTube and Display, including UK political ads with spend. | Open | Google | 2026-11-23 |
| [IPSO rulings](https://www.ipso.co.uk/rulings/) | Search rulings on complaints against newspapers and magazines that signed up to IPSO. *Some outlets, including the Guardian and FT, are not members.* | Open | Independent Press Standards Organisation (IPSO) | 2026-11-23 |
| [Media Reform Coalition](https://www.mediareform.org.uk/) | Read the regular report on who owns the UK's news media and how concentrated it is. *Campaign group based at Goldsmiths, University of London.* | Open | Media Reform Coalition | 2026-11-23 |
| [Meta Ad Library](https://www.facebook.com/ads/library/) | See every ad running on Facebook and Instagram, and political ads in the UK with spend, reach and who paid. *Meta returned a 403 to our script; loads in a browser.* | Open | Meta | 2026-11-23 (not reachable from our checker) |
| [Ofcom Broadcast and On Demand Bulletin](https://www.ofcom.org.uk/tv-radio-and-on-demand/broadcast-standards/broadcast-bulletins) | Read Ofcom's rulings on complaints against TV and radio programmes, including breaches and sanctions. | Open | Office of Communications (Ofcom) | 2026-11-23 |

## FOI, documents and archives

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [British Newspaper Archive](https://www.britishnewspaperarchive.com/) | Search scanned pages of British and Irish newspapers from the 1700s to the 2000s. *A security check blocked our checker; loads in a browser. Searching is free, viewing pages needs a subscription.* | Paid | Findmypast in partnership with the British Library | 2026-11-23 (not reachable from our checker) |
| [GOV.UK FOI releases](https://www.gov.uk/search/transparency-and-freedom-of-information-releases?content_store_document_type=foi_release) | Search FOI responses that departments publish as disclosure logs, to see what has already been released. *Only some departments publish their FOI responses; councils and NHS bodies keep their own disclosure logs.* | Open | UK government departments (via GOV.UK) | 2026-11-23 |
| [Historic Hansard 1803-2005](https://api.parliament.uk/historic-hansard/index.html) | Browse two centuries of parliamentary debates by date, person or constituency. *Older digitisation with some gaps and errors; use Hansard for recent years.* | Open | UK Parliament | 2026-11-23 |
| [ICO decision notices](https://ico.org.uk/action-weve-taken/decision-notices/) | Read the regulator's rulings on FOI complaints, showing what public bodies tried to withhold and why. | Open | Information Commissioner's Office (ICO) | 2026-11-23 |
| [National Archives Discovery](https://discovery.nationalarchives.gov.uk/) | Search the catalogue of UK government records at The National Archives and over 2,500 other archives, including newly released Cabinet and ministry files. *Most records are catalogue entries only; many files must be viewed in Kew or ordered as copies.* | Open | The National Archives | 2026-11-23 |
| [Scottish Information Commissioner decisions](https://www.foi.scot/decisions) | Read decisions on FOI appeals against Scottish public bodies, which work under separate Scottish FOI law. | Open | Scottish Information Commissioner | 2026-11-23 |
| [UK Government Web Archive](https://webarchive.nationalarchives.gov.uk/) | See old versions of UK government websites and social media accounts, including pages that were changed or deleted. | Open | The National Archives | 2026-11-23 |
| [UK Web Archive](https://www.webarchive.org.uk/) | Search archived copies of UK websites collected by the British Library and other legal deposit libraries. *Much of the collection can be viewed only in the reading rooms of the legal deposit libraries.* | Open | British Library and UK legal deposit libraries | 2026-11-23 |
| [Wayback Machine](https://web.archive.org/) | See past versions of websites, useful for recovering deleted pages from companies, campaigns and officials. | Open | Internet Archive (nonprofit) | 2026-11-23 |
| [WhatDoTheyKnow](https://www.whatdotheyknow.com/) | Send Freedom of Information requests to UK public bodies and search hundreds of thousands of past requests and the documents released. *A bot check blocked our checker; loads in a browser. Searching is open; sending a request needs a free account.* | Free login | mySociety (charity) | 2026-11-23 (not reachable from our checker) |

## Investigative outlets and research groups

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [Bellingcat](https://www.bellingcat.com/) | Learn open-source investigation methods and read investigations into conflicts, disinformation and the far right, with step-by-step guides. | Open | Bellingcat (Netherlands-based foundation) | 2026-11-23 |
| [Bureau of Investigative Journalism](https://www.thebureauinvestigates.com/) | Read UK-based investigations into money, power, health and environment, many with published datasets. | Open | The Bureau of Investigative Journalism (charity) | 2026-11-23 |
| [Centre for Information Resilience](https://www.info-res.org/) | Read open-source investigations into conflicts, human rights abuses and information operations, including the Myanmar and Sudan Witness projects. | Open | Centre for Information Resilience (UK nonprofit) | 2026-11-23 |
| [Finance Uncovered](https://www.financeuncovered.org/) | Read investigations into tax, offshore money and corruption, and find training for journalists on following the money. | Open | Finance Uncovered (UK nonprofit) | 2026-11-23 |
| [Full Fact](https://fullfact.org/) | Check claims made by UK politicians and in the media against official data, with the sources linked. | Open | Full Fact (charity) | 2026-11-23 |
| [ICIJ Offshore Leaks Database](https://offshoreleaks.icij.org/) | Search offshore companies, trusts and their officers from the Panama Papers, Paradise Papers, Pandora Papers and other leaks, with many UK and Crown Dependency links. *Published newsroom leak database; appearing in it is not proof of wrongdoing.* | Open | International Consortium of Investigative Journalists (ICIJ) | 2026-11-23 |
| [Liberty Investigates](https://libertyinvestigates.org.uk/) | Read human rights investigations into policing, immigration, surveillance and state power, made with partner newsrooms. | Open | Liberty (human rights charity) | 2026-11-23 |
| [Lighthouse Reports](https://www.lighthousereports.com/) | Read collaborative investigations with European newsrooms, including on migration, surveillance and algorithms, often involving the UK. | Open | Lighthouse Reports (Netherlands-based nonprofit) | 2026-11-23 |
| [Open Ownership](https://www.openownership.org/en/) | Read research and guidance on beneficial ownership registers, including the UK PSC register and its weaknesses. *Its old Open Ownership Register address now redirects to an explainer page.* | Open | Open Ownership (nonprofit) | 2026-11-23 |
| [Private Eye](https://www.private-eye.co.uk/) | Follow long-running reporting on business, councils, the press and Westminster, including the Rotten Boroughs and In the City columns. *Most reporting is in the print magazine; only selected pieces are online.* | Partly paid | Pressdram Ltd | 2026-11-23 |
| [Spotlight on Corruption](https://www.spotlightcorruption.org/) | Read research on UK anti-corruption enforcement, sanctions breaches, dirty money and the performance of the SFO and other agencies. | Open | Spotlight on Corruption (charity) | 2026-11-23 |

## Tools and search techniques

| Source | What you can find | Access | Run by | Checked |
|---|---|---|---|---|
| [archive.today](https://archive.ph/) | Save and look up snapshots of web pages, including some pages the Wayback Machine cannot capture. *Connection timed out from our script; often shows a captcha in browsers.* | Captcha | archive.today (anonymous operator) | 2026-11-23 (not reachable from our checker) |
| [Bellingcat OpenStreetMap search](https://osm-search.bellingcat.com/) | Find places where certain features appear close together on OpenStreetMap, such as a church next to a railway and a river, to geolocate an image. *Depends on how well the area is mapped.* | Open | Bellingcat | 2026-11-23 |
| [crt.sh](https://crt.sh/) | Search certificate transparency logs to find subdomains and related websites registered to an organisation. *Returned a 502 error to our script today; the service is often overloaded and usually comes back.* | Open | Sectigo | 2026-11-23 (not reachable from our checker) |
| [ExifTool](https://exiftool.org/) | Read hidden metadata in photos, videos and documents, such as camera, software, time and GPS location. *Social platforms strip most metadata on upload.* | Open | Phil Harvey (open source) | 2026-11-23 |
| [Google Advanced Search](https://www.google.com/advanced_search) | Narrow Google results by site, file type, exact phrase and date, for example finding PDFs on gov.uk or a council site. | Open | Google | 2026-11-23 |
| [InVID-WeVerify plugin](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/) | Use a browser plugin to split videos into keyframes, run reverse image searches and check metadata to verify footage. | Open | InVID / WeVerify consortium, maintained by AFP | 2026-11-23 |
| [Nominet WHOIS lookup](https://nominet.uk/lookup/) | Look up the registrar, registration dates and status of any .uk domain name. *nominet.uk/whois now redirects here. Registrant names of individuals are usually hidden.* | Open | Nominet | 2026-11-23 |
| [Shodan](https://www.shodan.io/) | Find internet-connected devices and servers, such as exposed cameras or control systems, by organisation or location. *Filters and bulk results need a paid account.* | Partly paid | Shodan LLC | 2026-11-23 |
| [TinEye](https://tineye.com/) | Reverse search an image to find where else it has appeared online and its oldest known copy. | Open | Idée Inc. | 2026-11-23 |

## Contributing

Corrections matter more than additions. If a link has moved, a portal has started charging, or a description is wrong, please open an issue or a pull request.

To add a source, add an object to `research/entries.json` with these fields and run `python3 build_readme.py`:

```json
{
  "category": "Courts, tribunals and law",
  "name": "Name of the source",
  "url": "https://...",
  "what": "One sentence on what a journalist can find there.",
  "access": "open | free login | captcha | paid | partly paid",
  "run_by": "Who runs it",
  "status": "ok | unreachable | changed",
  "checked": "YYYY-MM-DD",
  "note": "Optional caveat"
}
```

Please open the link yourself on the day you add it, and keep to the scope above: no people-search services and nothing built on breached personal data.

## Related

- [india-osint](https://github.com/Ghongha007/india-osint): public records and open data for investigating India
- [china-osint](https://github.com/Ghongha007/china-osint): public records and open data for investigating China
- [russia-osint](https://github.com/Ghongha007/russia-osint): public records and open data for investigating Russia
- [usa-osint](https://github.com/Ghongha007/usa-osint): public records and open data for investigating the United States
- [ukraine-osint](https://github.com/Ghongha007/ukraine-osint): public records and open data for investigating Ukraine
- [ai-for-osint](https://github.com/Ghongha007/ai-for-osint): AI tools for investigators, with where each runs and its known limits
- [groundline](https://github.com/Ghongha007/groundline): check every sentence of a draft or AI summary against its source documents
- [chat2net](https://github.com/Ghongha007/chat2net): turn a chat or social-media export into a Gephi network
- [osint-skills](https://github.com/Ghongha007/osint-skills): agent skills for verification, geolocation, chronolocation and fact-checking
- [verify-mcp](https://github.com/Ghongha007/verify-mcp): an MCP server with keyless, read-only verification lookups

## Licence

The list is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The script is MIT. Compiled by [OSINT JOURNO](https://github.com/OSINT-JOURNO).
