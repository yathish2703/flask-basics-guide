# Why UV?

This project uses [uv](https://github.com/astral-sh/uv) instead of traditional `pip` and `requirements.txt` for several compelling reasons:

## 🚀 Benefits of UV

### ⚡ Speed
- **10-100x faster** than pip for package installation
- Written in Rust for maximum performance
- Parallel downloads and installations

### 🔒 Reliability
- **Lock file** (`uv.lock`) ensures reproducible builds
- Guarantees everyone uses the exact same dependency versions
- Prevents "works on my machine" issues

### 🎯 Simplicity
- **Single command** to set up everything: `uv sync`
- Automatically creates and manages virtual environments
- No need to manually create/activate venv

### 📦 Modern Package Management
- Compatible with `pyproject.toml` (PEP 621 standard)
- Better dependency resolution
- Clear dependency tree visualization

## 🆚 UV vs Traditional Approach

### Traditional (pip + requirements.txt)
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
```

### Modern (uv)
```bash
uv sync                    # Creates venv + installs dependencies
uv run python app.py       # Runs in isolated environment
```

## 📋 Common UV Commands

### Setup

**Install UV:**

```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# With pip (all platforms)
pip install uv

# With Homebrew (macOS)
brew install uv
```

**Install dependencies (first time):**
```bash
uv sync
```

### Running Python
```bash
# Run Python scripts
uv run python app.py
uv run python -m flask run

# Run any command in the virtual environment
uv run flask --version
```

### Managing Dependencies
```bash
# Add a package
uv add flask-mail

# Add development dependency
uv add --dev pytest

# Remove a package
uv remove flask-mail

# Update all packages
uv sync --upgrade

# Update specific package
uv add flask@latest
```

### Virtual Environment
```bash
# Activate virtual environment (if needed)
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# uv automatically uses .venv when you run commands with "uv run"
```

## 🔍 Understanding uv.lock

The `uv.lock` file:
- Lists **exact versions** of all dependencies and sub-dependencies
- Should be **committed to git**
- Ensures everyone gets the same environment
- Automatically updated when you add/remove packages

## 📦 pyproject.toml

This is the modern Python project configuration file:
- Replaces `requirements.txt`
- Follows PEP 621 standard
- Contains project metadata and dependencies
- More structured and maintainable

Example from this project:
```toml
[project]
name = "flask-basics-guide"
version = "1.0.0"
requires-python = ">=3.9"
dependencies = [
    "flask>=3.1.2",
    "flask-sqlalchemy>=3.1.1",
    "flask-wtf>=1.2.2",
    "flask-login>=0.6.3",
]
```

## 🔄 Migrating from requirements.txt

If you have an existing project:

1. **Install uv**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Initialize uv project**
   ```bash
   uv init --no-workspace
   ```

3. **Import from requirements.txt** (optional)
   ```bash
   uv add $(cat requirements.txt)
   ```

4. **Or add packages manually**
   ```bash
   uv add flask flask-sqlalchemy flask-wtf
   ```

## 🎓 Best Practices

1. **Commit uv.lock** to version control
   - Ensures reproducible deployments
   - Team uses same dependency versions

2. **Use `uv run` for scripts**
   - No need to activate venv manually
   - Cleaner CI/CD pipelines

3. **Regular updates**
   ```bash
   uv sync --upgrade  # Update all packages
   ```

4. **Dev dependencies**
   ```bash
   uv add --dev pytest black ruff  # Development tools
   ```

## 🚀 Deployment

UV works great in production:

```dockerfile
# Dockerfile example
FROM python:3.12-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copy project files
COPY . /app
WORKDIR /app

# Install dependencies
RUN uv sync --frozen --no-dev

# Run application
CMD ["uv", "run", "python", "app.py"]
```

## 📚 Learn More

- [UV Documentation](https://docs.astral.sh/uv/)
- [UV GitHub](https://github.com/astral-sh/uv)
- [Why UV is Fast](https://astral.sh/blog/uv)

---

**UV makes Python dependency management fast, reliable, and simple! 🎉**
