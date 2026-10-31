# Contributing to UtsavAI

Thank you for your interest in contributing to **UtsavAI – The Cultural & Multi-Scale Event Architect**! We welcome contributions that expand our cultural databases, enhance accessibility, bolster security, or optimize event engineering algorithms.

---

## 🛠️ Development Setup

1. **Clone Repository:**
   ```bash
   git clone https://github.com/Tirth3929v/utsavai.git
   cd utsavai
   ```

2. **Create Virtual Environment:**
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux / macOS:
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install pytest pytest-cov
   ```

4. **Run Application:**
   ```bash
   streamlit run app.py
   ```

---

## 🧪 Testing & Quality Standards

All pull requests must pass the automated test suite before merging:

```bash
# Run full unit and regression test suite
python -m pytest tests/test_engines.py -v

# Run smoke test
python tests/test_smoke.py
```

### Code Style Guidelines
- Follow **PEP 8** style guidelines with a maximum line length of 120 characters.
- Use **Type Annotations** (`typing.Dict`, `typing.List`, `typing.Optional`) on all function signatures.
- Provide clear **PEP 257** docstrings (`Args:`, `Returns:`, `Raises:`) on all public classes and methods.
- Commit messages should adhere to the [Conventional Commits](https://www.conventionalcommits.org/) specification (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`).

