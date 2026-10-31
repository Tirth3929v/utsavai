# Security Policy – UtsavAI

The UtsavAI project adheres to enterprise security standards, defensive credential isolation, zero-trust AI client boundaries, and strict data sanitization across all interactive event planning workflows.

## Supported Versions

| Version | Supported          | Security Maintenance Status |
| ------- | ------------------ | --------------------------- |
| 2.0.x   | :white_check_mark: | Active production & LTS     |
| 1.0.x   | :x:                | Deprecated                  |

---

## 🛡️ Security Pillars & Architectural Safeguards

### 1. API Key & Credential Isolation
- **Multi-Source Dynamic Resolution:** UtsavAI loads credentials strictly through runtime environment variables (`os.getenv`), secure Streamlit Secrets (`st.secrets`), or voluntary session-scoped UI overrides.
- **Zero Disk Persistence of Secrets:** API keys entered through the UI are never serialized, written to disk, or committed to version control.
- **Git Hygiene:** `.gitignore` enforces strict exclusion of `.env`, `.secrets`, `.pem`, and credential files.

### 2. Cross-Site Scripting (XSS) Prevention & HTML Sanitization
- All dynamic data rendered via `st.markdown(..., unsafe_allow_html=True)` is rigorously sanitized with `html.escape()` prior to DOM injection.
- Unsanitized user inputs or LLM-generated strings cannot inject executable scripts, iframe exploits, or arbitrary HTML tags.

### 3. Theological & Prompt Injection Defense
- UtsavAI uses an isolated multi-tiered system prompt architecture with strict JSON schema boundaries (`response_mime_type="application/json"`).
- Deterministic anti-hallucination sanitizers (`_sanitize_theological_schedule`) actively detect and purge cross-theological contamination before rendering.

### 4. Zero Data Harvesting & Privacy
- User event planning data (guest lists, budget figures, family names) is stored purely in ephemeral `st.session_state` memory and is never shared, logged, or retained externally.

---

## Reporting a Vulnerability

If you discover a potential security vulnerability within UtsavAI, please report it privately:

1. **Email:** Send details to `security@utsavai.org` or open a private GitHub Security Advisory.
2. **Response SLA:** We acknowledge receipt within **24 hours** and provide a patch timeline within **72 hours**.
3. **Disclosure:** Please refrain from publicly disclosing issues until an official patch has been published.
