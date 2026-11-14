# Flame in Freefall: Space Apps 2026 team guide

Nov 10, 2026 · @Lama Abou Khalil

## Today, Saturday 14 November

The hackathon is live, the data is open, and the Project tab on our team page unlocks at 9:00 in the Team Owner's local time.

- [ ] 15-minute call: lock the four must-haves and assign owners
- [ ] Data owner: open the [PSI combustion search](https://psi.nasa.gov/physci/repo/search?q=combustion) and list the roughly 22 Combustion Science investigations with their PSI ids
- [ ] Data owner: for each one, capture the Description fields and the Experimental Table; skip the raw video
- [ ] Dashboard owner: put a bare page on a public link and a public code repository
- [ ] SI owner: get one investigation summarized with a citation back to its PSI page and DOI
- [ ] Demo owner: open the Project tab after 9:00, turn the edit lock on, and start filling the form; save often
- [ ] Everyone: note every SI tool, dataset, library and image used as we go, for the references field
- [ ] Tonight: one end-to-end run, from scenario to ranked, cited investigations

## Key facts

The hackathon runs Saturday and Sunday, and our submission is due Sunday at 23:59 in the team creator's local time.

| Item | Detail |
| --- | --- |
| Team | Data Beyond Space ([team page](https://www.spaceappschallenge.org/2026/find-a-team/dataspace/)) |
| Challenge | [Flame in Freefall: SI-Powered Fire Safety Insights from Microgravity Combustion Data](https://www.spaceappschallenge.org/2026/challenges/flame-in-freefall/) |
| Difficulty | Intermediate / Advanced |
| Event | [Universal Event](https://www.spaceappschallenge.org/2026/local-events/universal-event/) (virtual, asynchronous) |
| Local Lead | Chris, NASA GO Team, info@spaceappschallenge.org |
| Challenge resources and datasets released | Nov 13, 2026 |
| Project Submission Guide and Judging & Awards Guide released | Nov 13, 2026 |
| Hackathon | Nov 14, 2026 to Nov 15, 2026 |
| Submission deadline | Nov 15, 2026, 23:59 local time of whoever created the team |
| Global Nominees, Finalists, Honorable Mentions | Nominees 3 December 2026; Finalists and Honorable Mentions 17 December 2026 |
| Global Winners | 26 January 2027 |

NASA's site uses "Super Intelligence (SI)" where we would say AI; it is the same thing.

Open question: who created the team on the site? Their time zone sets our deadline.

## Rules that can cost us eligibility

The biggest one: the FAQ says teams may not begin working on the challenge before the hackathon. Until Saturday we read, plan and learn tools; we do not write project code, build the dashboard or prepare the dataset.

- **Team size.** Universal Event teams need at least 2 members to be judged globally, and no team may exceed 6.
- **Same event.** Every member must be registered for the 2026 hackathon and signed up to the Universal Event, and must appear on the team's Members tab.
- **One team, one challenge.** Each person is on one team; each team works on one challenge.
- **SI disclosure.** The submission must describe how SI tools were used in development. This is confirmed for 2026.
- **Submit on the site.** Only a project submitted through the team's project page on spaceappschallenge.org is judged.
- **Under 18s.** Minors must be registered by a parent or guardian and must not appear in photos, video or voice in the submission.
- **Space Apps Connect.** Posting in the [GitHub Discussions forum](https://github.com/nasa/spaceapps/) confirms you registered and accepted the terms. It closes when the hackathon ends.

The 2026 Project Submission Guide confirms these and adds more; see Judging and submission below.

If we are unsure whether a piece of preparation counts as starting early, we ask Chris by email before doing it.

## What the challenge asks for

The deliverable is an interactive, SI-powered, web-based dashboard that summarizes, ranks and interprets NASA's microgravity combustion investigations to give fire safety insights for human spaceflight.

The problem NASA states is that the results in its Physical Sciences Informatics (PSI) database are hard to find, harder to compare and harder still to interpret. The dashboard should fix those three things.

NASA suggests, but does not require, that users can:

1. Identify the investigations most relevant to fire safety in crewed environments: spacecraft, stations, lunar and Martian bases, pressurized rovers.
2. Extract data that supports predictive modeling of flammability and fire scenarios.
3. Highlight research that informs next-generation fire safety controls and equipment.

Other points from the statement:

- **Audience:** professors, graduate and undergraduate students, aerospace researchers and engineers.
- **Attributes worth showing per investigation:** objectives; fuels and sample or burner shape and size; test conditions such as oxygen concentration and airflow speed; what varied between tests; sensors and measurement types.
- **Comparison:** show similarities and differences between investigations.
- **Earth applications are welcome:** water-mist extinguishers, smoke detection, firefighter gear.
- **Out of scope:** rocket and propellant fire safety.
- **Known gap:** PSI holds no partial-gravity combustion data yet. NASA says microgravity and normal-gravity results could bound what happens at lunar or Martian gravity.

Our team page says we will train ML models on the combustion data. The statement puts summarizing, ranking and interpreting first and treats predictive modeling as one optional feature, so the dashboard and the investigation catalogue should come before any model.

## Domain cheat sheet

In microgravity there is no buoyancy, so hot gas does not rise; a candle flame becomes a blue sphere fed by diffusion. NASA's spacecraft fire safety work has three pillars: prevention, detection and suppression.

Everything in this section comes from the challenge statement.

| Investigation | Fuel type | Hardware | Fire safety pillar |
| --- | --- | --- | --- |
| BASS, BASS-II (Burning and Suppression of Solids) | Solids such as fabrics and plastics | Microgravity Science Glovebox (MSG), SPICE flow duct | Prevention (flammability) |
| Saffire-I, -II, -III (Spacecraft Fire Safety Demonstration) | Solids | Not stated | Prevention (flammability) |
| SAME, SAME-R (Smoke and Aerosol Measurement Experiment) | Smoke | Not stated | Detection |
| FLEX, FLEX-2 (Flame Extinguishment Experiment) | Liquid fuel droplets | MDCA in the Combustion Integrated Rack (CIR) | Suppression (CO2 and helium dilution) |
| CFI (Cool Flames Investigation) | Liquid fuel droplets | MDCA in the CIR | Less direct |
| ACME, six experiments including BRE, CFI-G, E-FIELD Flames | Gaseous fuels | ACME modular hardware in the CIR | BRE: material flammability in still atmospheres |
| SPICE, SLICE | Solid and gaseous fuels across the MSG group | MSG, SPICE flow duct | Less direct |
| DAFT, DAFT-2 | Dust, not smoke | Same instrument as SAME | Related detection hardware |

Oxygen facts that make a strong story:

- Spacesuits run 100% oxygen at 4.3 psi; Earth sea level is 14.7 psi.
- The Moon Base and pressurized rovers are expected to sit in between: 30% oxygen or more, at 10.2 psi or less.
- That is over a 40% increase in oxygen concentration compared with Earth, which makes materials much more flammable.
- The highest oxygen tests in microgravity were in CFI-G, with up to 85% oxygen flowing from a spherical burner.
- E-FIELD Flames mimicked partial gravity through an electric field acting on flame ions.
- Future partial-gravity experiments named by NASA: LUCI and FM2.

Real incidents NASA cites for the pitch: Apollo 1 (1967), Apollo 13, the Mir oxygen generator fire, and a smoke alarm on Artemis II.

## Data

The data source NASA names is the [PSI Data Repository, combustion search](https://psi.nasa.gov/physci/repo/search?q=combustion); it opened for me without a login and returns 26 investigations, about 22 of them in Combustion Science.

Each investigation page, for example [PSI-25, BASS-II](https://psi.nasa.gov/physci/repo/data/investigations/PSI-25), holds:

- **Description:** project type, flight platform, dates, objectives, approach, hypothesis, research impacts and Earth benefits, sub-research area such as Spacecraft Fire Safety, related investigations.
- **Experimental Table:** one row per test. BASS-II has 130 rows with fuel sample material, flow settings, and initial and final oxygen, CO2 and CO readings.
- **Hardware**, representative images, and a publications list with DOIs.
- **Data files:** engineering documents, raw data, reference data, science documents, reports. BASS-II totals 255.77 GB, mostly video.
- **DOI and license:** BASS-II is CC0-1.0. PSI requires citing each investigation by its DOI, using the "Cite this Investigation" link.

What this means for us:

- The Description fields and Experimental Tables are small, structured and exactly the attributes the challenge asks us to compare. Build the catalogue from them.
- Do not download raw data; it is far too large for a weekend.
- The Experimental Tables give real oxygen and flow values per test, which is what the ranking and the coverage map need.
- Show the DOI beside every investigation in the dashboard. It satisfies PSI's citation rule and helps the Validity score.

| PSI id | Investigation | Type |
| --- | --- | --- |
| [PSI-26](https://psi.nasa.gov/physci/repo/data/investigations/PSI-26) | BASS | Microgravity |
| [PSI-25](https://psi.nasa.gov/physci/repo/data/investigations/PSI-25) | BASS-II | Microgravity |
| [PSI-98](https://psi.nasa.gov/physci/repo/data/investigations/PSI-98) | Saffire-I | Microgravity |
| [PSI-99](https://psi.nasa.gov/physci/repo/data/investigations/PSI-99) | Saffire-II | Microgravity |
| [PSI-100](https://psi.nasa.gov/physci/repo/data/investigations/PSI-100) | Saffire-III | Microgravity |
| [PSI-102](https://psi.nasa.gov/physci/repo/data/investigations/PSI-102) | SAME | Microgravity |
| [PSI-101](https://psi.nasa.gov/physci/repo/data/investigations/PSI-101) | SAME-R | Microgravity |
| [PSI-69](https://psi.nasa.gov/physci/repo/data/investigations/PSI-69) | FLEX | Microgravity |
| [PSI-68](https://psi.nasa.gov/physci/repo/data/investigations/PSI-68) | FLEX-2 | Microgravity |
| [PSI-39](https://psi.nasa.gov/physci/repo/data/investigations/PSI-39) | CFI | Microgravity |
| [PSI-20](https://psi.nasa.gov/physci/repo/data/investigations/PSI-20) | ACME BRE | Microgravity |
| [PSI-159](https://psi.nasa.gov/physci/repo/data/investigations/PSI-159) | ACME CFI-G | Microgravity |
| [PSI-22](https://psi.nasa.gov/physci/repo/data/investigations/PSI-22) | ACME E-FIELD Flames | Microgravity |
| [PSI-10](https://psi.nasa.gov/physci/repo/data/investigations/PSI-10) | ACME Flame Design | Microgravity |
| [PSI-21](https://psi.nasa.gov/physci/repo/data/investigations/PSI-21) | ACME CLD Flame | Microgravity |
| [PSI-23](https://psi.nasa.gov/physci/repo/data/investigations/PSI-23) | ACME spherical diffusion flames | Microgravity |
| [PSI-107](https://psi.nasa.gov/physci/repo/data/investigations/PSI-107) | SPICE | Microgravity |
| [PSI-106](https://psi.nasa.gov/physci/repo/data/investigations/PSI-106) | SLICE | Microgravity |
| [PSI-117](https://psi.nasa.gov/physci/repo/data/investigations/PSI-117), [PSI-142](https://psi.nasa.gov/physci/repo/data/investigations/PSI-142), [PSI-62](https://psi.nasa.gov/physci/repo/data/investigations/PSI-62), [PSI-60](https://psi.nasa.gov/physci/repo/data/investigations/PSI-60), [PSI-115](https://psi.nasa.gov/physci/repo/data/investigations/PSI-115) | Ground studies that reuse PSI flight data | Ground |

The search has a second page with one more result that I did not open, and I read only the BASS-II page in full; other investigations may be laid out differently.

Other resources NASA lists for the challenge:

- [NASA Combustion Science](https://www.nasa.gov/glenn/glenn-expertise-space-exploration/physical-sciences-program/combustion-science/): basics on most of the investigations in PSI
- [A Researcher's Guide to ISS Combustion Science](https://www.nasa.gov/missions/station/a-researchers-guide-to-combustion-science/): a 2015 review
- [ScienceCasts video on ISS combustion](https://www.youtube.com/watch?v=W1oXykoz9zg): a 3.6-minute introduction
- Incidents: [Apollo 1](https://sma.nasa.gov/sma-disciplines/accllp/apollo-1), [Apollo 13](https://sma.nasa.gov/sma-disciplines/accllp/apollo-13), [Mir fire](https://www.nasa.gov/history/25-years-ago-fire-aboard-space-station-mir/)
- Earth spinoffs: [firefighter air tanks](https://spinoff.nasa.gov/node/9582), [fire detector](https://spinoff.nasa.gov/node/9407), [firefighter clothing](https://spinoff.nasa.gov/node/9918)

## Judging and submission

Judges mainly read the project page, so the written submission matters as much as the product. Everything below is confirmed against the 2026 guides dated 13 November.

### How judging works

1. Universal Event judges compare our project only against other Universal Event projects and pick Global Nominees. The number of nominees is proportional to the number advancing from Local Events.
2. NASA and partner experts review the nominees and choose Global Finalists and Honorable Mentions.
3. An executive committee picks the 10 Global Winners.

### Criteria (each scored 1 to 5 at every judging level)

| Criterion | What judges ask (paraphrased) | How we score on it |
| --- | --- | --- |
| Impact | How far could it reach, and is the problem big? | Tie every insight to Moon Base and rover crew safety at 30%+ oxygen |
| Creativity | Is the approach new, or a small step on existing work? | Go beyond a search box: ranking, side-by-side comparison, gap finder |
| Validity | Is it scientifically sound and workable in practice? | Every SI answer cites its PSI investigation; no invented numbers |
| Relevance | Does it answer the challenge, and is it complete and usable? | Cover summarize, rank and interpret, the three verbs in the statement |
| Presentation | Is the challenge, solution and importance told clearly? | One person owns the demo from Saturday morning |

Relevance now explicitly rewards NASA data used as a core part of the solution, not a superficial addition; Validity also covers completeness and usability. The guide warns that teams tend to neglect Presentation, which is judged on both the demo and the full project page.

### Awards we fit best

Of the [10 Global Awards](https://www.spaceappschallenge.org/awards/), three match this project: Best Use of Data (makes space data accessible), Best Use of Science (valid use of science) and Best Use of Technology (innovative technology).

### Submission form

- Fields: project name, high-level summary, demo link, final project link, detailed description, NASA data used, other data and tools used, use of SI, verification.
- Demo: a video of at most 30 seconds with English subtitles, or at most 7 slides including the title slide. Going over makes the project ineligible.
- Demo and project must sit on public links needing no login. Test them in a private browser window.
- Everything in English.
- SI-generated images and video need a visible watermark; SI-generated code, audio and data must be acknowledged in text. SI output must not use NASA logos or mission identifiers.
- List every external resource used; work must be original.
- Submission is final; nothing saved after the deadline counts.

New or clarified in the 2026 guide:

- The Project tab appears on the team page at 9:00 on Saturday in the Team Owner's local time; submission closes Sunday 23:59 in the same time zone.
- We can edit and resubmit as often as we like until the deadline; judges see only the last saved submission. Submit an early version on Sunday afternoon, then improve it.
- To be eligible for a Global Award the project must use at least one NASA data source or resource. PSI covers this.
- SI may speed up the work but should not be used to come up with the idea for solving the challenge.
- The "Use of SI" answer is for data collection and is not shown to judges, but judges do see watermarks and SI acknowledgements inside the project and assess originality from them.
- No new members can be added after submission closes.
- No images, video or audio of anyone under 18 in the demo or project.
- Optional: if the project is on a new website, request a FortiGuard web filter classification so judges are less likely to be blocked.
- Two people editing the Project tab can overwrite each other; use the edit lock and agree who is editing.

## Recommended scope

This section is my recommendation, not something from NASA: build a cited investigation explorer first, and add one small predictive feature only if time allows.

Must have, in build order:

1. **Investigation catalogue.** One structured record per combustion investigation with the attributes NASA lists: objective, fuel, sample geometry, oxygen range, airflow, hardware, sensors, fire safety pillar.
2. **Relevance ranking.** The user picks a scenario, for example "lunar habitat, 34% oxygen, 8.2 psi, fabric", and the dashboard ranks investigations by how closely their test conditions match, with the reasons shown.
3. **Compare view.** Two or three investigations side by side: what is shared, what differs.
4. **SI interpretation with citations.** A language model answers questions over the catalogue and linked documents, and every claim links back to its PSI investigation.

Good additions if the first four work:

- A coverage map of oxygen concentration against pressure or flow speed, showing where data exists and where the expected Moon Base atmosphere falls. Gaps are an insight in themselves.
- A simple, interpretable flammability model on one clean dataset, such as flame spread or extinction against oxygen and flow. State its limits plainly.
- An "on Earth" tab linking findings to terrestrial fire safety.

Why not lead with ML training: the data is likely to be mixed formats and small per experiment, a weekend is short, and Validity is judged. A modest model with honest limits beats an impressive one nobody can verify.

Suggested roles for a team of up to six: data and catalogue lead, SI and retrieval lead, front end and data visualization, domain reader (physics or chemistry), demo and story owner, and one person who owns the submission form and deadline.

## Plan

Before Saturday we prepare people and knowledge only; the build starts when the hackathon does. Times below are my suggestion; the official opening time for submissions should be in Friday's guide.

### Now until Thursday

- [ ] Confirm every member is registered, in the Universal Event and listed on the team's Members tab
- [ ] Find out who created the team and note their time zone
- [ ] Everyone reads the challenge statement and this guide
- [ ] Assign the six roles
- [ ] Open PSI and learn how it is organized and whether it needs an account
- [ ] Read NASA background on BASS, Saffire, SAME and FLEX
- [ ] Agree the tech stack and who has which accounts and API keys
- [ ] Look at 2025 winning project pages to see what a strong submission looks like
- [ ] Check Space Apps Messages on the site for updates from the GO Team

### Friday 13 November

- [ ] Read the challenge Resources tab the moment it opens
- [ ] Read the Project Submission Guide and the Judging & Awards Guide; correct this doc where 2026 differs
- [ ] Lock the scope: the four must-haves

### Saturday 14 November

1. Morning: pull the data, build the catalogue schema, fill it for the eight to ten most fire-relevant investigations.
2. Midday: bare dashboard showing the catalogue; SI summarization working on one investigation.
3. Afternoon: ranking and compare view.
4. Evening: end-to-end run on a public link. Demo owner drafts the story.

### Sunday 15 November

1. Morning: citations on every SI answer; coverage map if the core is stable.
2. Early afternoon: feature freeze. Fix, polish, write the project page.
3. Late afternoon: record the 30-second video or finish the 7 slides; write the SI disclosure and data lists.
4. Evening: test all links in a private window and submit hours before 23:59, not minutes.

## Sources

- [Flame in Freefall challenge page](https://www.spaceappschallenge.org/2026/challenges/flame-in-freefall/)
- [2026 Challenges](https://www.spaceappschallenge.org/2026/challenges/)
- [Participant FAQs, 5 November 2026](https://www.spaceappschallenge.org/resources/participant-faqs/)
- [Universal Event page](https://www.spaceappschallenge.org/2026/local-events/universal-event/)
- [Awards](https://www.spaceappschallenge.org/awards/)
- [Resources and participant guides](https://www.spaceappschallenge.org/resources/)
- [Project Submission Guide, 2025 edition](https://www.spaceappschallenge.org/resources/project-submission-guide/)
- [Judging & Awards Guide, 2024 edition](https://spaceappschallenge.org/resources/judging-awards-guide)
- [Space Apps Connect on GitHub](https://github.com/nasa/spaceapps/)
- [NASA PSI overview](https://science.nasa.gov/?p=158684)
- [NASA Science Data blog on PSI](https://science.data.nasa.gov/learn/blog/psi-spotlight)
- [NASA technical report on PSI data](https://ntrs.nasa.gov/citations/20150002323)
