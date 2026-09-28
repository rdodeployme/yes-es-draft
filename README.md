# YES · Yindyamarra Environmental Sustainability (unlisted draft)

**Status: unlisted draft v0.1. Not for public use. Demo data only.** Every page carries `noindex`, and `robots.txt` disallows crawling.

YES is a monthly environmental reporting service for councils first, then businesses and government. Customers send their bills, dockets, statements and registers each month. **YES enters every raw figure** (litres, kilowatt-hours, kilolitres, tonnes, hectares and counts), and a second YES analyst verifies the month. YES then calculates everything else: emissions, rates, intensities, trends, targets and the **Yindyamarra Environmental Score**. The score is one of the key reports YES provides to councils.

## Cultural protocol (read before changing anything)

- **The name.** *Yindyamarra* is a Wiradjuri word, used with the permission of Wiradjuri language custodians. Confirm with them the translation wording the site uses ("often translated as respect, gentleness and taking responsibility") and whether they wish to be acknowledged by name.
- **Other Aboriginal words.** No other Aboriginal words are used. Each word belongs to its own nation and needs its own permission.
- **The logo.** It is to be designed by an Aboriginal artist and has not been commissioned yet.
- **The Country film.** It is to be commissioned with Traditional Owners, paid for and approved by the people in it.
- **The river footage.** The clip in the Country section is a placeholder only. It shows no people.
- **No AI or imitation work.** Do not add AI-generated or imitation Aboriginal art, symbols or patterns, and no depictions of Aboriginal people.

## Pages

| Path | What it is |
|---|---|
| `/` | Home |
| `/score/` | The Yindyamarra Environmental Score: bands, direction of travel, provisional rules and a live sample |
| `/portal/` | The working customer portal prototype (see below) |
| `/data-dictionary/` | Every field and calculated figure, with filters and a CSV download |
| `/method/` | Formulas, factor tables, scoring rules, evidence grades, limits |
| `/contact/` | Contact by email only (contact@yes.com.au). There is no phone line. |

## The portal prototype

The portal is a static single-page app. Everything is kept in the visitor's browser: `localStorage` holds the figures and IndexedDB holds documents and evidence files. Nothing is sent to a server.

- **Who does what.**
  - **Customers** see their verified months, send documents and download their data. They never key figures.
  - **YES data entry** keys every figure from the customer's documents and attaches the evidence.
  - **YES verification** is a different person who checks each figure against its document, grades the evidence (A, B or C), and verifies the month or returns it to data entry with a note. The person who entered a month cannot verify it.
- **Sign-in.** Demo accounts only, with no passwords:
  - three fictional organisations: Demo Shire Council (VIC), Demo Coastal Council (NSW) and Demo Freight Co. (QLD);
  - two YES team accounts: Morgan Lee (data entry) and Chris Walker (verification).
- **Customer dashboard.** It shows verified months only:
  - the Yindyamarra Environmental Score, with year-on-year and month-on-month change;
  - ten category tiles with sparklines;
  - emissions by scope, including avoided emissions reported separately;
  - targets against actuals and the key rolling 12-month figures;
  - the fleet and data quality;
  - where the next month stands (entered and awaiting verification, or documents due).
- **Send documents.** Upload by month and category; uploads open the month for YES data entry. Customers can also email documents.
- **Where you could be.** The dashboard shows three numbers: the score **now**, the score **at the organisation's own targets**, and an **estimate with YES help** (the recommended work done), with the tonnes of CO₂-e behind it.
- **Recommended for you.** Published rules (`assets/js/recommend.js`) turn the figures into up to ten kinds of help, weakest category first. Each card shows why, the estimated change and who delivers it, with a **Book a session** button.
- **Roadmap and help.** The three numbers, the last 12 months of scores with the projection and a target line, the plan (items can be switched off), the plan by quarter, and the customer's bookings with the change in the category score since completed work (a change, not a claim of cause).
- **Booking.** Pick a slot over the next ten business days, the format, contact details and notes, and choose whether to share the figures behind the recommendation. Nothing is sent in the prototype.
- **Reports.** A printable three-page A4 monthly report for each verified month. Page 3 is the roadmap: the three numbers, the projected score, the plan by quarter, progress so far, and disclosure of any Recycle Group work.
- **Data.** CSV and JSON export for customers. YES can import CSV/JSON into months open for data entry. The demo can be reset.
- **YES team.**
  - Data entry: open months across customers, the customer's documents beside the form, only the fields due that month (monthly; quarterly in Sep, Dec, Mar and Jun; annual in June; static registers carried forward), live calculations, warnings for figures more than 35% away from last year or last month, evidence attached or picked from the customer's documents.
  - Verification queue, bookings (confirm, mark done, cancel), customer list, factor library and activity log.
  - The team also sees months waiting for verification on dashboards, marked provisional.

## How it is built

- `assets/js/dictionary.js`: the YES Data Dictionary (fields, units, frequencies, sources, mandatory status, calculations and which scores they feed).
- `assets/js/engine.js`: the calculation engine. It holds the factors, monthly calculations, seasonal baseline comparison, rolling 12 months, scores and targets.
- `assets/js/recommend.js`: the recommendation rules, their assumed effects, the score at target and with YES help, and the roadmap projection.
- `assets/js/demo-data.js`: a seeded generator for the fictional demo organisations, with demo bookings.
- `assets/js/portal.js` with `assets/css/portal.css`: the portal app.
- `assets/css/yes.css` holds the design system and `assets/css/pages.css` the marketing-page styles.
- `_src/build.py`: wraps the page fragments in `_src/pages/` in the shared shell and writes the site.

  ```
  python3 _src/build.py                 # served under /yes-es-draft/ (GitHub Pages)
  YES_BASE=/ python3 _src/build.py      # served at a domain root, e.g. yes.com.au
  ```

## Method v0.1 (a draft for discussion)

- **Emissions factors.** DCCEEW National Greenhouse Accounts Factors 2024, as reproduced in the Commonwealth Emissions Reporting Framework 2024–25. Electricity is location-based, by state.
- **Scope 3.** Covers the categories reported here only: waste to landfill, and upstream fuel, gas and electricity.
- **Council boundary.** Council waste figures include the municipal kerbside service (garbage, recycling, food and garden organics, glass) and transfer stations, as well as council operations.
- **Flights.** Recorded, but not converted to emissions until a factor is adopted.
- **Avoided emissions.**
  - Modelled with NSW DECCW (2010) factors, which are flagged as dated.
  - Reported separately; they are never netted and never an offset.
- **The score.**
  - It is the mean of the category scores that have data.
  - Trend comparisons use the same calendar months of the baseline year.
  - Target-based categories are provisional until 12 months of data exist.
  - A month is provisional until a second YES analyst verifies it; customers see it once verified.
- **Targets, potential and help.** The score at target treats each target in the profile as met. The score with YES help applies the published assumed effect of each recommended item. Items start two a quarter (booked items in their booked month) and build up over six months. Recycle Group work is disclosed, any provider can be used, and a YES analyst who runs a paid session does not enter or verify that customer's months.
- **Claims.**
  - The score is self-declared under the published method. It is not an accredited rating, certification or offset.
  - The score with YES help and the projection are estimates, not promises.
  - No carbon neutral, net zero or offset claims are made from YES figures.

## Before this becomes a real product

1. **Commissions.** The logo by an Aboriginal artist and the Country film with Traditional Owners. Confirm the Yindyamarra wording with the custodians who gave permission.
2. **Authentication.** Real accounts: single sign-on or emailed sign-in links, with roles for customers, YES data entry and YES verification.
3. **Server-side data.** A database built from the data dictionary, evidence file storage, an audit log, and versioned factors with recalculation.
4. **Method review.** Score weights and bands, a flight factor, and refreshed avoided-emissions factors.
5. **Hosting.** Attach the yes.com.au domain and confirm the contact@ mailbox.
