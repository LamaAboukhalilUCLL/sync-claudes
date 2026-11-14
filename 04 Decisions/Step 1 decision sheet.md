# Step 1 decision sheet

**Added:** Sat 14 Nov 2026, 18:25 · **By:** Vic, with Claude (Cowork)

A one-page aid for the call where the team chooses the central insight. It holds **only verified facts, their limits, and the criteria to judge by**. It proposes no insight. Space Apps rule: AI must not come up with the idea, so the insight, and the sentence that states it, are the team's (Lama decides, see D1).

## The sentence to fill in
> "Our dashboard shows that ______, so engineers and crews planning [habitat] should ______."

Once this exists, the 2-3 views, the data fields for Step 2 and the demo story follow from it.

## Verified facts
All already checked against `app/raw/`. Source note in brackets.

| # | Fact | Limit |
|---|---|---|
| 1 | **Solids were tested near Earth-air oxygen.** BASS-II 13.6-22.2 % (0 of 129 rows at 30 % or more); Saffire-I about 21.5 %; Saffire-II about 21.5-22.1 %. BASS-II's approach says oxygen was "varied below 21%". [[PSI data source]], [[Oxygen evidence (generated)]] | BASS and Saffire-III state **no** oxygen in their tables, so the pattern is unverified for them |
| 2 | **30 % ambient oxygen or more appears only for gases and droplets:** FLEX (24 of 274 rows, up to 34 %), FLEX-2 (30 % listed for every fuel), CFI-G normal flames (115 of 179, up to 40 %), Flame Design normal flames (131 of 207, up to 40 %), BRE (34 or 40 % on all 16 readable test days), s-Flame (about 30 % on 8 of 18 test days). [[PSI data source]] | CFI-G and Flame Design's **85 % is burner-flow oxygen**, not an atmosphere (D5) |
| 3 | **Target atmospheres:** challenge statement, Moon Base and pressurized rovers at 30 % or more and 10.2 psi or less. PSI-20 lists three "NASA-considered" atmospheres: 21 % / 14.7 psia, 26.5 % / 10.2 psia, 34 % / 8.2 psia. Oxygen partial pressure is about the same in all (2.7-3.1 psi, our arithmetic); the concentration is what rises. [[Vetted reference from the external briefs]] §1 | PSI never labels any atmosphere "Moon Base" or "Mars". "More flammable because of concentration" still needs a citable source |
| 4 | **Why oxygen rises:** NASA says on camera that higher habitat oxygen lowers decompression-sickness risk and allows more frequent spacesuit activity, and that this has implications for material flammability. [[Challenge video]] | A reason, not data |
| 5 | **BRE, research impacts:** burning continued "despite the absence of air flow", notably in elevated-oxygen atmospheres, "whereas such flames in a normal atmosphere of 21% oxygen self-extinguished in a short time". Cutting ventilation is an established step in putting out spacecraft fires. [[Vetted reference from the external briefs]] §2 | One investigation's own summary text; BRE is a gas burner emulating solids. Its 16 publications have not been read |
| 6 | **Earth-gravity screening:** NASA-STD-6001 Test 1 "segregates material based on 1-g behavior without consideration of low gravity effects" (PSI-26). BASS hypothesizes materials in ventilated microgravity "burn as well if not better" (PSI-26). [[Vetted reference from the external briefs]] §2 | Hypotheses and stated impacts, not measured results |
| 7 | **Saffire-II is the only table pairing microgravity and 1-g burns**, and it cuts both ways: thin silicone burned completely in 1 g and not in microgravity; SIBAL burned 29 cm in microgravity and completely in 1 g. [[Vetted reference from the external briefs]] §3 | 9 sample rows, about 21.5-22 % oxygen only |
| 8 | **Detection:** without buoyancy, smoke particles grow larger, which may stop some detectors alarming (SAME, SAME-R hypothesis). [[Vetted reference from the external briefs]] §2 | Hypothesis; small tables; no oxygen variation |
| 9 | **No PSI combustion record mentions partial gravity, the Moon or Mars.** [[Vetted reference from the external briefs]] §2 | Rules out any insight that needs partial-gravity data |
| 10 | **Coverage:** only 10 of 24 investigations state an ambient oxygen value in their table, in mixed units and formats. [[Vetted reference from the external briefs]] §8 | - |

## Criteria to score each candidate insight
| Criterion | Question |
|---|---|
| Validity | Can every claim be traced to `app/raw/` **tonight**? If it needs papers we have not read, can someone read them by Sunday morning? |
| Relevance | Does it serve all three asks: find relevant investigations, extract data for prediction, highlight research for fire safety controls? |
| Impact | Is the crew-safety consequence clear in one sentence? |
| Creativity | Does the dashboard show something PSI's own site cannot? |
| Presentation | Can it be told on one slide? |
| Buildable | Can its 2-3 views be done by Sunday 17:00? |

A candidate that fails Validity tonight is out, however strong it sounds.

## Call plan (30 min)
1. **10 min:** read facts 1, 2, 5 and 7 together (screen-share [[Oxygen evidence (generated)]] section 1 and the Saffire-II table).
2. **10 min:** each person names a candidate sentence; score them against the criteria out loud.
3. **5 min:** Lama writes the final sentence and adds it to [[Decision log]] as a new entry, "Decided by: Lama".
4. **5 min:** derive from it the 2-3 views, the fields Step 2 needs, the demo format, and one owner per track (data, dashboard, AI layer, project page and demo).

See also: [[Status]], [[Decision log]].
