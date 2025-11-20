# 🎯 Quick Start Guide

Get the Flask Basics Guide running in 5 minutes!

## Step 1: Install UV ⚡

Pick your platform and copy-paste the command:

### 🍎 macOS
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 🐧 Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 🪟 Windows
Open **PowerShell** and run:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 🐍 Alternative (Any Platform)
If you already have Python:
```bash
pip install uv
```

---

## Step 2: Verify Installation ✅

Close and reopen your terminal, then:

```bash
uv --version
```

Expected output: `uv 0.5.x` (or similar)

**If it doesn't work:** See [INSTALL_UV.md](INSTALL_UV.md) for troubleshooting.

---

## Step 3: Clone the Project 📥

```bash
# Clone the repository
git clone <repository-url>
cd flask-basics-guide

# Or if you downloaded a ZIP, extract and cd into it
```

---

## Step 4: Install Dependencies 📦

One command does it all:

```bash
uv sync
```

This will:
- ✅ Create a virtual environment (`.venv`)
- ✅ Install Flask and all dependencies
- ✅ Generate a lock file (`uv.lock`)

**Time:** ~5 seconds (vs. 30-60 seconds with pip!)

---

## Step 5: Set Up Environment 🔧

```bash
# Copy the example environment file
cp .env.example .env

# (Optional) Edit .env with your preferred settings
# nano .env  # or use any text editor
```

---

## Step 6: Run the App 🚀

```bash
uv run python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

---

## Step 7: Open in Browser 🌐

Visit: **http://localhost:5000**

You'll see the Flask Basics Guide homepage with all modules!

---

## 🎉 You're Done!

### What to Explore:

1. **Basic Routes** (`/basic`) - Learn routing basics
2. **Templates** (`/templates`) - Jinja2 templating
3. **Forms** (`/forms`) - Form handling & validation
4. **Database** (`/database`) - SQLAlchemy & CRUD
5. **Authentication** (`/auth`) - User login & sessions
6. **API** (`/api`) - RESTful API endpoints

---

## 📝 Common Commands

```bash
# Run the app
uv run python app.py

# Add a new package
uv add package-name

# Update packages
uv sync --upgrade

# Open Python REPL
uv run python

# Run any Python script
uv run python script.py
```

---

## ❓ Troubleshooting

### "uv: command not found"
- **Solution:** Restart your terminal after installation
- **Still broken?** Check [INSTALL_UV.md](INSTALL_UV.md)

### "Port 5000 already in use"
- **Solution:** Edit `app.py` and change port:
  ```python
  app.run(debug=True, port=5001)
  ```

### Import errors
- **Solution:** Make sure to use `uv run`:
  ```bash
  uv run python app.py  # ✅ Correct
  python app.py         # ❌ Wrong
  ```

### Need to reset database?
```bash
uv run python -c "from app import app, db; app.app_context().push(); db.drop_all(); db.create_all()"
```

---

## 📚 Next Steps

1. ✅ **Complete** - You have the app running!
2. 📖 **Learn** - Explore each module in the browser
3. 💻 **Code** - Try the examples in [LEARNING_PATH.md](LEARNING_PATH.md)
4. 🚀 **Build** - Create your own Flask project!

---

## 🆘 Need More Help?

- 📖 [Full Installation Guide](INSTALL_UV.md)
- 🔧 [Quick Reference](QUICK_REFERENCE.md)
- ❓ [Why UV?](WHY_UV.md)
- 🔄 [Migrating from pip](MIGRATION_TO_UV.md)
- 🎓 [Learning Path](LEARNING_PATH.md)

---

**Happy Flask Learning! 🎉**

Made with ❤️ for beginners
