# Business Model Canvas – **json‑lingo**

| **Key Partners** | **Key Activities** | **Key Resources** |
|------------------|--------------------|-------------------|
| • **AI model providers** – vLLM, SGLang (open‑source inference engines) | • Develop & maintain the JSON translation engine (parsing, schema‑aware translation, post‑edit validation) | • Proprietary translation pipeline code (repo) |
| • **Localization platforms** – Transifex, Lokalise, Phrase | • Integrate with popular i18n frameworks (React‑Intl, i18next, Flutter Intl) | • Access to Axentx’s curated multilingual datasets (auto, instr‑resp, messages, query‑resp) |
| • **Cloud providers** – AWS, GCP, Azure (for scalable inference) | • Continuous model fine‑tuning on domain‑specific corpora | • Hosted inference endpoints (vLLM) |
| • **Open‑source community** – contributors to JSON schema tools | • QA & automated testing (schema validation, round‑trip consistency) | • Documentation & SDKs (npm, pip, Maven) |
| • **Enterprise customers** – Mobile/web app vendors | • Customer support & onboarding (integration guides, webinars) | • Sales & marketing assets (use‑case videos, case studies) |

| **Value Proposition** | **Customer Segments** |
|-----------------------|-----------------------|
| • **AI‑powered, schema‑aware JSON translation** – 1‑click conversion of resource files into any target language while preserving structure. | • **App developers** building multilingual mobile/web apps (React, Vue, Flutter, Android, iOS). |
| • **Error reduction** – Automatic detection of missing keys, placeholder mismatches, and pluralization rules. | • **Product teams** that need rapid localisation for feature releases. |
| • **Cost & time savings** – Eliminates manual copy‑paste and reduces reliance on external translation agencies. | • **Localization agencies** looking to augment human translators with AI pre‑translation. |
| • **Seamless CI/CD integration** – CLI & GitHub Action that runs on pull‑request, ensuring new strings are always translated. | • **Enterprise SaaS platforms** that expose UI strings to third‑party developers. |
| • **Extensible SDKs** – npm, pip, Maven packages for easy embedding in build pipelines. | • **Open‑source projects** seeking a free, community‑driven translation helper. |

| **Channels** | **Revenue Streams** |
|--------------|---------------------|
| • **Developer portals** – npm, PyPI, Maven Central listings. | • **Subscription SaaS** – tiered plans (Starter, Professional, Enterprise) based on translation volume (tokens) and SLA. |
| • **GitHub Marketplace** – Action for automated PR translation. | • **Pay‑as‑you‑go** – usage‑based billing for on‑demand inference (per 1 M characters). |
| • **Web dashboard** – self‑serve onboarding, API keys, usage analytics. | • **Enterprise licensing** – on‑premise deployment with dedicated VPC & custom model fine‑tuning. |
| • **Partner integrations** – plugins for Android Studio, Xcode, VS Code. | • **Professional services** – custom schema design, domain‑specific model training, migration assistance. |
| • **Content marketing** – blog posts, webinars, case studies on multilingual app ROI. | • **Marketplace add‑ons** – premium language packs (e.g., Japanese‑formal, Arabic‑dialects). |

| **Cost Structure** |
|--------------------|
| • **Cloud compute** – GPU/CPU inference costs (vLLM hosting). |
| • **Data licensing & curation** – maintaining multilingual pair datasets (auto, instr‑resp, messages, query‑resp). |
| • **Engineering salaries** – core team (backend, ML, dev‑ops). |
| • **Partner commissions** – revenue share with localization platforms & marketplace. |
| • **Customer support & success** – SLA staffing for Enterprise tier. |
| • **Security & compliance** – audits, GDPR/CCPA tooling. |
| • **Marketing & sales** – developer outreach, events, ads. |

---  

*Prepared for the **json‑lingo** product (Automated JSON translation tool for multilingual app development) using Axentx’s internal datasets and verified AI inference frameworks.*
