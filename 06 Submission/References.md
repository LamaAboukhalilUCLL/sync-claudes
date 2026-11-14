# References

Everything external the project uses goes here, with link text and URL, even if free.

## NASA data and resources
| Link text | URL | Used for |
|---|---|---|
| PSI Data Repository: Combustion Science | https://psi.nasa.gov/physci/repo/search?q=combustion | Investigation metadata and Experimental Tables |
| 2026 Challenge: Flame in Freefall (NASA Space Apps video) | https://www.youtube.com/watch?v=AVuEiKxOpc0 | Understanding the challenge; reason for higher habitat oxygen ([[Challenge video]]) |

### The 24 Combustion Science investigations, cited by DOI
Collected from the `doi` field of each record in `app/raw/` on 14 Nov 2026. Clicking the DOI links has not been tested yet.

| Link text | URL | Used for |
|---|---|---|
| PSI-10: ACME/Flame Design - Advanced Combustion via Microgravity Experiments / Flame Design | https://doi.org/10.60555/w4zy-bt45 | Metadata record and Experimental Table |
| PSI-20: ACME BRE - Advanced Combustion via Microgravity Experiments - Burning Rate Emulator | https://doi.org/10.60555/vb93-3y72 | Metadata record and Experimental Table |
| PSI-21: ACME CLD Flame - Advanced Combustion via Microgravity Experiments / Coflow Laminar Diffusion Flame | https://doi.org/10.60555/23e1-9950 | Metadata record and Experimental Table |
| PSI-22: ACME E-FIELD Flames - Advanced Combustion via Microgravity Experiments Electric-Field Effects on Laminar Diffusion Flames | https://doi.org/10.60555/se5a-8c73 | Metadata record and Experimental Table |
| PSI-23: ACME s-Flame - Advanced Combustion via Microgravity Experiments-Structure and Response of Spherical Diffusion Flames | https://doi.org/10.60555/k57n-p030 | Metadata record and Experimental Table |
| PSI-25: BASS-II - Burning and Suppression of Solids - II | https://doi.org/10.60555/4qc4-de67 | Metadata record and Experimental Table |
| PSI-26: BASS - Burning and Suppression of Solids | https://doi.org/10.60555/58h4-dy80 | Metadata record and Experimental Table |
| PSI-39: CFI - Cool Flames Investigation | https://doi.org/10.60555/m6pj-a914 | Metadata record and Experimental Table |
| PSI-47: DAFT / DAFT-2 - Dust and Aerosol Measurement Feasibility Test / Dust and Aerosol Measurement Feasibility Test-2 | https://doi.org/10.60555/ztgj-d202 | Metadata record and Experimental Table |
| PSI-60: Computational and Experimental Analysis of SPICE Data Sets | https://doi.org/10.60555/mzjm-yv57 | Metadata record (no Experimental Table) |
| PSI-62: Concurrent Flame Spread Modeling using Flamelet Generated Manifolds in Microgravity with Comparison to BASS Experiments using Two-Color Tomography | https://doi.org/10.60555/e9xp-ex83 | Metadata record (no Experimental Table) |
| PSI-68: FLEX-2 - Flame Extinguishment Experiment - 2 | https://doi.org/10.60555/byp8-h018 | Metadata record and Experimental Table |
| PSI-69: FLEX - Flame Extinguishment Experiment | https://doi.org/10.60555/mbq8-0451 | Metadata record and Experimental Table |
| PSI-98: SAFFIRE-I - Spacecraft Fire Safety Experiment-I | https://doi.org/10.60555/0t15-1z43 | Metadata record and Experimental Table |
| PSI-99: SAFFIRE-II - Spacecraft Fire Experiment-II | https://doi.org/10.60555/2chp-m469 | Metadata record and Experimental Table |
| PSI-100: SAFFIRE-III - Spacecraft Fire Experiment-III | https://doi.org/10.60555/040q-4h36 | Metadata record and Experimental Table |
| PSI-101: SAME-R - Smoke Aerosol Measurement Experiment-Reflight | https://doi.org/10.60555/2np7-jv14 | Metadata record and Experimental Table |
| PSI-102: SAME - Smoke and Aerosol Measurement Experiment | https://doi.org/10.60555/gd4k-8h62 | Metadata record and Experimental Table |
| PSI-106: SLICE - Structure and Liftoff In Combustion Experiment | https://doi.org/10.60555/pm12-rg61 | Metadata record and Experimental Table |
| PSI-107: SPICE - Smoke Point In Co-flow Experiment | https://doi.org/10.60555/9kbh-e962 | Metadata record and Experimental Table |
| PSI-115: Utilization of the Smoke Aerosol Measurement Experiment Data for Advanced Modeling and Simulation of Smoke Generation in Micro-Gravity | https://doi.org/10.60555/q0v5-1v28 | Metadata record (no Experimental Table) |
| PSI-117: Effect of External Thermo-Convective Perturbation on Cool Flame Dynamics: A Multidimensional Multi-Physics CFD Analysis | https://doi.org/10.60555/gz0q-b577 | Metadata record (no Experimental Table) |
| PSI-142: Quantitative Studies of Cool Flame Transitions at Radiation / Stretch Extinction Using Counterflow Flames | https://doi.org/10.60555/80qf-vj95 | Metadata record and Experimental Table |
| PSI-159: ACME CFI-G - Advanced Combustion via Microgravity Experiments / Cool Flames Investigation with Gases | https://doi.org/10.60555/cyt1-kh64 | Metadata record and Experimental Table |

## Other data, code, libraries, images, text
| Link text | URL | Used for |
|---|---|---|
| Python 3 standard library (no third-party packages) | https://docs.python.org/3/library/ | `app/fetch_snapshot.py`, `app/evidence_oxygen.py`, `fetch_papers.py` |
| OpenAlex (CC0 scholarly metadata) | https://openalex.org | Titles and abstracts for the publication DOIs listed in PSI ([[Publications and abstracts]]). Keep only if abstracts are used in the product |
