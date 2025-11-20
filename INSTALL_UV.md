# UV Installation Guide

Complete installation instructions for UV on all platforms.

## 📦 What is UV?

UV is an extremely fast Python package and project manager, written in Rust. It's designed to be a drop-in replacement for pip, pip-tools, and virtualenv, but 10-100x faster.

## 🖥️ Installation Methods

### Method 1: Standalone Installer (Recommended)

#### **macOS and Linux**

Open your terminal and run:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

This will:
- Download the latest UV binary
- Install it to `~/.cargo/bin/uv`
- Add the directory to your PATH

#### **Windows**

Open **PowerShell** as Administrator and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

This will:
- Download the latest UV binary
- Install it to `%USERPROFILE%\.cargo\bin\uv.exe`
- Add the directory to your PATH

### Method 2: pip (All Platforms)

If you already have Python and pip installed:

```bash
pip install uv
```

**Pros:** Simple, uses familiar tool  
**Cons:** Requires Python already installed, slower than standalone

### Method 3: Homebrew (macOS)

If you use Homebrew:

```bash
brew install uv
```

### Method 4: Cargo (All Platforms)

If you have Rust's cargo installed:

```bash
cargo install --git https://github.com/astral-sh/uv uv
```

### Method 5: Package Managers

#### **Linux - apt (Debian/Ubuntu)**
```bash
# Add the repository
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### **Linux - yum/dnf (RHEL/Fedora)**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### **Arch Linux**
```bash
# UV is available in AUR
yay -S uv
# or
paru -S uv
```

## ✅ Verify Installation

After installing, **restart your terminal** and verify:

```bash
uv --version
```

You should see output like:
```
uv 0.5.x
```

## 🔧 Post-Installation Setup

### Update PATH (if needed)

If `uv --version` doesn't work, you may need to add UV to your PATH:

#### **macOS and Linux**

Add to `~/.bashrc`, `~/.zshrc`, or `~/.profile`:

```bash
export PATH="$HOME/.cargo/bin:$PATH"
```

Then reload:
```bash
source ~/.bashrc  # or ~/.zshrc
```

#### **Windows**

1. Press `Win + X` and select "System"
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Under "User variables", find "Path"
5. Click "Edit" and add: `%USERPROFILE%\.cargo\bin`
6. Click "OK" and restart your terminal

## 🚀 First Steps

Once UV is installed, test it:

```bash
# Check version
uv --version

# Get help
uv --help

# Create a new project
uv init my-project
cd my-project

# Add a package
uv add flask

# Run Python
uv run python --version
```

## 🆙 Updating UV

Keep UV up to date:

### **Standalone Installation**

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### **pip Installation**

```bash
pip install --upgrade uv
```

### **Homebrew**

```bash
brew upgrade uv
```

### **Self-Update (if available)**

```bash
uv self update
```

## 🐛 Troubleshooting

### "uv: command not found"

**Solution:**
1. Restart your terminal
2. Check if UV is in your PATH (see "Update PATH" above)
3. Verify installation directory exists:
   - Unix: `ls ~/.cargo/bin/uv`
   - Windows: `dir %USERPROFILE%\.cargo\bin\uv.exe`

### Permission Denied (macOS/Linux)

**Solution:**
```bash
# Make UV executable
chmod +x ~/.cargo/bin/uv
```

### Windows SmartScreen Warning

**Solution:**
Click "More info" → "Run anyway". UV is safe and open source.

### SSL Certificate Errors

**Solution:**
```bash
# Update your system's CA certificates
# macOS
brew install ca-certificates

# Ubuntu/Debian
sudo apt-get update
sudo apt-get install ca-certificates

# Fedora
sudo dnf install ca-certificates
```

### Behind a Corporate Proxy

**Solution:**
Set proxy environment variables:

```bash
# Unix
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080

# Windows (PowerShell)
$env:HTTP_PROXY="http://proxy.example.com:8080"
$env:HTTPS_PROXY="http://proxy.example.com:8080"
```

## 🔄 Uninstalling UV

If you need to remove UV:

### **Standalone Installation**

```bash
# macOS/Linux
rm ~/.cargo/bin/uv

# Windows (PowerShell)
Remove-Item $env:USERPROFILE\.cargo\bin\uv.exe
```

### **pip Installation**

```bash
pip uninstall uv
```

### **Homebrew**

```bash
brew uninstall uv
```

## 📚 Additional Resources

- [Official UV Documentation](https://docs.astral.sh/uv/)
- [UV GitHub Repository](https://github.com/astral-sh/uv)
- [UV Discord Community](https://discord.gg/astral-sh)
- [Migration Guide](https://docs.astral.sh/uv/pip/compatibility/)

## 💡 Tips

1. **Use the standalone installer** for best performance
2. **Restart your terminal** after installation
3. **Update regularly** to get latest features and fixes
4. **Check the docs** for advanced configuration options

---

**Ready to use UV? Head back to the [README.md](README.md) to set up the Flask project!** 🚀
