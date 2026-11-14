# AI provider and hosting options

**Added:** Sat 14 Nov 2026 · **By:** Vic, with Claude (Cowork)

Input for two open decisions: the **AI provider** (Step 5, deferred by D9) and the **hosting** (Step 3). Options only; nothing here is decided.

## What the Space Apps Global Offers give us
From the Global Offers page (logged-in view, 14 Nov 2026):
- **GitHub Copilot Free:** coding assistant only (2,000 completions per month, limited chat and agent use). The app cannot call it.
- **Microsoft Copilot:** a chat app, no API.
- **Microsoft Azure:** $200 credit for 30 days for new customers. Phone and a credit/debit card needed for identity checks.
- **Google Cloud:** $300 credit for 90 days. Card asked for verification; no automatic charge after the trial.
- **GoDaddy Registry:** free non-premium domain plus one year of hosting and SSL, registered through Porkbun.
- Microsoft Teams, Planetary Computer, Meteomatics, Miro: not relevant to the AI layer.

**None of the offers is a ready-to-use model API.** Also: **GitHub Models was retired on 30 July 2026** ([GitHub docs](https://docs.github.com/en/github-models/use-github-models/prototyping-with-ai-models)), so a GitHub account no longer gives free model access.

## AI provider options
| Option | Cost and catch | Fit |
|---|---|---|
| Gemini API free tier (Google AI Studio) | No card. Free Flash models. Community-reported limits are roughly 10 requests per minute and 1,500 per day per project; **indicative only, check in AI Studio**. Free-tier terms and EU availability not checked. | Enough for answers generated in advance |
| Google Cloud credit (Global Offer) | Gemini through Vertex AI, higher limits. Card for verification. | Backup if free-tier limits block us |
| Azure credit (Global Offer) | OpenAI models through Azure AI Foundry. Card and phone. Which models a trial subscription can use was **not verified**. | Only if someone already knows Azure |

Whatever the provider:
- **Answers generated in advance** from the saved records, stored in a file the static site reads, need no key at runtime and cannot hit rate limits during judging. This matches D9 and "static site first" in [[Vetted reference from the external briefs]].
- **Live questions** need a key, and the key must sit in a small server-side function, never in the browser or the repository (which becomes public).
- Whichever model is used goes in [[SI use log]].

## Hosting options
- **GitHub Pages:** free, serves a static site straight from the repository at `<user>.github.io/<repo>`. A GitHub **Release** is a download, not a website, so judges could not open it.
- **GoDaddy free domain:** optional, pointed at the Pages site. A new domain can be blocked by web filters; request the FortiGuard classification (see [[Rules and eligibility]]) and always also give the default `github.io` link.
- **No personal or hobby domain:** judges see the URL first, filters may block it, and the link must stay up through January 2027 judging.

See also: [[Publications and abstracts]], [[Decision log]].
