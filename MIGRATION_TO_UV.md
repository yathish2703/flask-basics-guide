# Migration to UV - Quick Start

If you previously used this project with `requirements.txt`, here's how to migrate:

## 🔄 Migration Steps

### 1. Install UV

Choose your platform:

**macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**With pip (any platform):**
```bash
pip install uv
```

**With Homebrew (macOS):**
```bash
brew install uv
```

**Verify installation:**
```bash
uv --version
```

### 2. Remove Old Virtual Environment (Optional)
```bash
rm -rf venv/  # Or whatever your venv folder was named
```

### 3. Install Dependencies with UV
```bash
uv sync
```

That's it! UV will:
- ✅ Create a new `.venv` directory
- ✅ Install all dependencies from `pyproject.toml`
- ✅ Generate a `uv.lock` file for reproducibility

## 📝 Command Changes

| Old Command (pip) | New Command (uv) |
|-------------------|------------------|
| `pip install -r requirements.txt` | `uv sync` |
| `python app.py` | `uv run python app.py` |
| `pip install flask-mail` | `uv add flask-mail` |
| `pip uninstall flask-mail` | `uv remove flask-mail` |
| `pip list` | `uv pip list` |

## 🎯 Quick Reference

```bash
# Setup (first time)
uv sync

# Run the app
uv run python app.py

# Add a package
uv add package-name

# Update packages
uv sync --upgrade
```

## ❓ FAQs

### Do I need to activate the virtual environment?
No! `uv run` automatically uses the `.venv` environment. But you can still activate it manually if preferred:
```bash
source .venv/bin/activate  # macOS/Linux
```

### Where did requirements.txt go?
Dependencies are now in `pyproject.toml` (modern Python standard). UV also generates `uv.lock` for exact version locking.

### Can I still use pip?
Yes, but UV is much faster and more reliable. If needed:
```bash
uv pip install package-name
```

### What about CI/CD?
UV works great in CI/CD:
```yaml
# GitHub Actions example
- name: Install uv
  run: curl -LsSf https://astral.sh/uv/install.sh | sh

- name: Install dependencies
  run: uv sync

- name: Run tests
  run: uv run pytest
```

## 🚀 Benefits You'll Notice

1. **Speed**: Installations are 10-100x faster
2. **Reliability**: Lock file ensures consistent environments
3. **Simplicity**: One command (`uv sync`) does everything
4. **Modern**: Uses `pyproject.toml` (Python standard)

## 🆘 Troubleshooting

### "Command not found: uv"
Restart your terminal after installing UV, or add to PATH:
```bash
export PATH="$HOME/.cargo/bin:$PATH"
```

### Import errors
Make sure to use `uv run`:
```bash
uv run python app.py  # ✅ Correct
python app.py         # ❌ Might not find packages
```

### Dependencies not found
Re-sync dependencies:
```bash
uv sync --reinstall
```

---

**Welcome to the faster world of UV! ⚡**
