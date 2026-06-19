# ROADMAP.md – **json‑lingo**

*Automated JSON translation tool for multilingual app development, leveraging Axentx’s AI stack to streamline and de‑risk the localization pipeline.*

---

## 📌 Vision  

Empower product teams to ship multilingual features faster by turning any JSON‑based resource file into a **high‑quality, context‑aware translation** with a single command or API call.  

- **Zero‑code integration** – CLI, library, and CI/CD plugin.  
- **AI‑driven accuracy** – leverage vLLM / SGLang models fine‑tuned on our `instr‑resp` and `messages` corpora.  
- **Safety & auditability** – placeholder preservation, change‑tracking, and reversible roll‑backs.  

---

## 📅 Milestones  

| Milestone | Target | Description | MVP‑Critical |
|-----------|--------|-------------|--------------|
| **MVP (Launch)** | Q3 2026 | Core end‑to‑end translation flow that can be used in production. | ✅ |
| **v1 – Production‑Ready Suite** | Q4 2026 | Feature set that satisfies most enterprise localization pipelines. | — |
| **v2 – Advanced Collaboration & Ops** | Q2 2027 | Team‑centric, observability, and extensibility layers. | — |
| **Future Horizons** | 2027+ | Marketplace, model‑as‑a‑service, and cross‑format support. | — |

---

## 🚀 MVP – Must‑Have for Launch  

| # | Feature | Acceptance Criteria | Notes |
|---|---------|----------------------|-------|
| **MVP‑1** | **JSON parser & extractor** | - Detect string values, keys, and ICU‑style placeholders (`{0}`, `{name}`) in any valid JSON file.<br>- Preserve original structure on output. | Built on Python’s `json` + custom AST for placeholder safety. |
| **MVP‑2** | **AI translation engine** | - Call a locally‑hosted vLLM model (e.g., `mistralai/Mistral-7B-Instruct`) to translate extracted strings.<br>- Support at least **English → Spanish, French, German** out‑of‑the‑box.<br>- Return confidence scores. | Model served via `vllm` inference server; prompt template stored in BRAIN. |
| **MVP‑3** | **Placeholder preservation** | - Ensure placeholders remain unchanged and correctly positioned in translated strings.<br>- Unit tests covering 100+ placeholder patterns. | Uses SGLang structured generation to enforce token constraints. |
| **MVP‑4** | **CLI tool** | - `json-lingo translate <input.json> --to fr --out output.fr.json`.<br>- Flags for batch mode, dry‑run, and confidence threshold. | Entry point `json_lingo/__main__.py`. |
| **MVP‑5** | **Basic caching** | - Store source‑string → translation mapping in a local SQLite DB to avoid re‑translation within a session. | Reduces cost & latency; cache invalidated on source change. |
| **MVP‑6** | **Error handling & logging** | - Graceful fallback to original string on model failure.<br>- Structured logs (JSON) for CI integration. | Uses Axentx logging standard. |
| **MVP‑7** | **CI/CD plugin (GitHub Action)** | - Action that runs on PRs, translates changed JSON files, and posts a summary comment with diffs. | Demonstrates “plug‑and‑play” for early adopters. |
| **MVP‑8** | **Documentation & quick‑start guide** | - README with installation, usage examples, and troubleshooting.<br>- API reference generated via `mkdocstrings`. | Essential for adoption. |

> **MVP‑Critical** items are marked with ✅ in the table above. All other MVP items are required for a production‑grade launch but are not single‑point blockers.

---

## 🛠️ v1 – Production‑Ready Suite  

| Theme | Feature | Target Release | Description |
|-------|---------|----------------|-------------|
| **Multi‑language expansion** | Add **Japanese, Chinese (Simplified), Portuguese** support. | Q4 2026 | Extend model prompt library; add language‑specific tokenizers. |
| **Batch & streaming API** | HTTP REST endpoint (`/translate`) + WebSocket streaming for large payloads. | Q4 2026 | Enables integration with backend services and mobile CI pipelines. |
| **Advanced quality checks** | - Terminology glossary enforcement.<br>- Automatic back‑translation validation.<br>- Confidence‑threshold alerts. | Q4 2026 | Leverages `query‑resp` dataset for terminology extraction. |
| **Versioned translation bundles** | Produce `v{n}` bundles with changelog (added/removed keys). | Q4 2026 | Facilitates roll‑backs and audit trails. |
| **Enterprise auth & RBAC** | OAuth2 + role‑based permissions for API access. | Q4 2026 | Aligns with Axentx security standards. |
| **Extensible model plug‑in** | Interface to swap vLLM model with custom fine‑tuned checkpoint. | Q4 2026 | Future‑proofs for internal LLMs. |
| **Metrics & observability** | Prometheus exporter (requests, latency, error rates). | Q4 2026 | Ops visibility for SaaS customers. |

---

## 📈 v2 – Collaboration &
