# YES · Yindyamarra Environmental Sustainability (unlisted draft)

**Status: unlisted draft v0.1. Not for public use. Demo data only.** Every page carries `noindex`, and `robots.txt` disallows crawling.

YES is a monthly environmental reporting service. Councils first, then businesses and government, enter their raw operational figures once a month through a customer portal: litres, kilowatt-hours, kilolitres, tonnes, hectares and counts. YES calculates everything else: emissions, rates, intensities, trends, targets and the **Yindyamarra Environmental Score**. The score is one of the key reports YES provides to councils.

## Cultural protocol (read before changing anything)

- **Permission for the name.** *Yindyamarra* is a Wiradjuri word. It is not to be used at launch without the permission of Wiradjuri language custodians. The meaning we publish will be the one they give us.
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

The portal is a static single-page app. Everything is kept in the visitor's browser: `localStorage` holds the figures and IndexedDB holds attached evidence files. Nothing is sent to a server.

- **Sign-in.** Demo accounts only, with no passwords:
  - three fictional organisations: Demo Shire Council (VIC), Demo Coastal Council (NSW) and Demo Freight Co. (QLD);
  - a YES team account.
- **Dashboard.** It shows:
  - the Yindyamarra Environmental Score, with year-on-year and month-on-month change;
  - ten category tiles with sparklines;
  - emissions by scope, including avoided emissions reported separately;
  - targets against actuals and the key rolling 12-month figures;
  - the fleet and data quality.
- **Category detail.** Each category shows its score history, how it is scored, and the figures entered compared with last month and last year.
- **Monthly submission.**
  - The form shows only the fields due that month: monthly; quarterly in Sep, Dec, Mar and Jun; annual in June; and static registers carried forward.
  - YES calculations update live as the customer types.
  - A figure more than 35% away from the same month last year, or from last month when there is no year-ago figure, gets a warning.
  - Customers attach evidence for each category, then submit with an attestation.
- **Reports.** A printable two-page A4 monthly report.
- **Data.** CSV and JSON export, and CSV/JSON import into draft months only. The demo can be reset.
- **YES team.**
  - A review queue: flag figures, grade evidence (A, B or C), then verify the month or return it to the customer with a note.
  - A customer list, a factor library and an activity log.

## How it is built

- `assets/js/dictionary.js`: the YES Data Dictionary (fields, units, frequencies, sources, mandatory status, calculations and which scores they feed).
- `assets/js/engine.js`: the calculation engine. It holds the factors, monthly calculations, seasonal baseline comparison, rolling 12 months, scores and targets.
- `assets/js/demo-data.js`: a seeded generator for the fictional demo organisations.
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
- **Flights.** Recorded, but not converted to emissions until a factor is adopted.
- **Avoided emissions.**
  - Modelled with NSW DECCW (2010) factors, which are flagged as dated.
  - Reported separately; they are never netted and never an offset.
- **The score.**
  - It is the mean of the category scores that have data.
  - Trend comparisons use the same calendar months of the baseline year.
  - Target-based categories are provisional until 12 months of data exist.
  - A month is provisional until YES verifies it.
- **Claims.**
  - The score is self-declared under the published method. It is not an accredited rating, certification or offset.
  - No carbon neutral, net zero or offset claims are made from YES figures.

## Before this becomes a real product

1. **Permissions and commissions.** Get permission from Wiradjuri custodians for the name. Commission the logo and the Country film.
2. **Authentication.** Real accounts: single sign-on or emailed sign-in links, with roles for customers and YES staff.
3. **Server-side data.** A database built from the data dictionary, evidence file storage, an audit log, and versioned factors with recalculation.
4. **Method review.** Score weights and bands, the municipal waste boundary for councils, a flight factor, and refreshed avoided-emissions factors.
5. **Hosting.** Attach the yes.com.au domain and confirm the contact@ mailbox.
