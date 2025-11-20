# 🚀 Flask Basics Guide

A comprehensive, beginner-friendly Flask tutorial with separate modules for each concept. Perfect for learning Flask from scratch!

> **⚡ This project uses [uv](https://docs.astral.sh/uv/)** - an extremely fast Python package installer and resolver written in Rust. It's 10-100x faster than pip! See [WHY_UV.md](WHY_UV.md) for more details.

📚 **[Documentation Index](DOCS_INDEX.md)** - Find all guides and references

## 🚀 Quick Start

| Platform | Installation Command |
|----------|---------------------|
| **macOS/Linux** | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| **Windows** | `powershell -c "irm https://astral.sh/uv/install.ps1 \| iex"` |
| **With pip** | `pip install uv` |
| **With Homebrew** | `brew install uv` |

Then run: `uv sync` → `uv run python app.py`

📖 **New to this?** Start with the [Quick Start Guide](QUICKSTART.md) | **Detailed installation:** [INSTALL_UV.md](INSTALL_UV.md)

## 📚 What You'll Learn

This project covers all the essential Flask concepts:

1. **Basic Routes** - Routing, URL parameters, HTTP methods
2. **Templates** - Jinja2 templating, inheritance, filters, macros
3. **Forms** - Form handling, validation, Flask-WTF
4. **Database** - SQLAlchemy, models, CRUD operations
5. **Authentication** - User registration, login, session management
6. **API** - RESTful API creation with JSON responses
7. **Error Handling** - Custom error pages
8. **Static Files** - CSS, JavaScript, and asset management

## 🛠️ Installation

### Prerequisites

- Python 3.9 or higher
- uv (fast Python package installer)

> 📖 **Need help installing UV?** See the detailed [UV Installation Guide](INSTALL_UV.md) for your platform.

### Install UV

Choose the installation method for your operating system:

#### **macOS and Linux**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### **Windows (PowerShell)**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### **With pip (all platforms)**
```bash
pip install uv
```

#### **With Homebrew (macOS)**
```bash
brew install uv
```

#### **With cargo (all platforms)**
```bash
cargo install --git https://github.com/astral-sh/uv uv
```

> **Note**: After installation, restart your terminal or add `~/.cargo/bin` (Unix) or `%USERPROFILE%\.cargo\bin` (Windows) to your PATH.

### Setup Steps

1. **Clone or download this repository**

2. **Verify UV is installed**
   ```bash
   uv --version
   ```

3. **Install dependencies and create virtual environment**
   ```bash
   uv sync
   ```
   
   This automatically creates a `.venv` directory and installs all dependencies.

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and update the values:
   - `SECRET_KEY` - A random secret key for session security
   - `DATABASE_URL` - Database connection string (default: SQLite)

5. **Run the application**
   ```bash
   uv run python app.py
   ```
   
   Or activate the virtual environment first:
   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   python app.py
   ```

6. **Open your browser**
   
   Navigate to: `http://localhost:5000`

## 📁 Project Structure

```
flask-basics-guide/
├── app.py                      # Main application file
├── pyproject.toml             # Project configuration & dependencies (uv)
├── uv.lock                    # Dependency lock file
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
│
├── modules/                   # Feature modules (blueprints)
│   ├── __init__.py
│   ├── basic_routes.py       # Module 1: Basic routing
│   ├── templates_module.py   # Module 2: Templates
│   ├── forms_module.py        # Module 3: Forms
│   ├── database_module.py     # Module 4: Database
│   ├── auth_module.py         # Module 5: Authentication
│   ├── api_module.py          # Module 6: REST API
│   └── error_handling.py      # Module 7: Error handling
│
├── templates/                 # HTML templates
│   ├── base.html             # Base template (layout)
│   ├── index.html            # Homepage
│   ├── templates_module/     # Templates for Module 2
│   ├── forms_module/         # Templates for Module 3
│   ├── database_module/      # Templates for Module 4
│   ├── auth_module/          # Templates for Module 5
│   └── errors/               # Error pages (404, 500, etc.)
│
└── static/                    # Static files
    ├── css/
    │   └── style.css         # Main stylesheet
    └── js/
        └── script.js         # Main JavaScript
```

## 📖 Module Guide

### Module 1: Basic Routes
**URL:** `/basic`

Learn about:
- Simple routes
- URL parameters (`/user/<username>`)
- Typed URL parameters (`/user/<int:user_id>`)
- Query strings (`?q=search`)
- HTTP methods (GET, POST, PUT, DELETE)
- Redirects

### Module 2: Templates
**URL:** `/templates`

Learn about:
- Passing variables to templates
- Control structures (if, for, while)
- Jinja2 filters
- Template inheritance
- Macros (reusable components)
- Static files integration

### Module 3: Forms
**URL:** `/forms`

Learn about:
- Basic HTML forms
- Flask-WTF integration
- Form validation
- CSRF protection
- Custom validators
- File uploads

### Module 4: Database
**URL:** `/database`

Learn about:
- SQLAlchemy setup
- Creating models
- CRUD operations (Create, Read, Update, Delete)
- Querying data
- Filtering and ordering
- Database relationships

### Module 5: Authentication
**URL:** `/auth`

Learn about:
- User registration
- Password hashing (secure)
- Login/logout
- Session management
- Protected routes (`@login_required`)
- Current user access

### Module 6: REST API
**URL:** `/api`

Learn about:
- Creating JSON endpoints
- RESTful API design
- HTTP status codes
- Request/response handling
- API documentation

**Example API Endpoints:**
- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create task
- `GET /api/tasks/<id>` - Get single task
- `PUT /api/tasks/<id>` - Update task
- `DELETE /api/tasks/<id>` - Delete task

### Module 7: Error Handling
**URL:** `/error`

Learn about:
- Custom error pages
- 404 Not Found
- 500 Internal Server Error
- 403 Forbidden
- Error handlers

## 🧪 Testing the API

You can test the API endpoints using curl or tools like Postman:

```bash
# Get all tasks
curl http://localhost:5000/api/tasks

# Create a task
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn Flask","priority":"high"}'

# Get single task
curl http://localhost:5000/api/tasks/1

# Update task
curl -X PUT http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed":true}'

# Delete task
curl -X DELETE http://localhost:5000/api/tasks/1

# Get API status
curl http://localhost:5000/api/status
```

## 💡 Key Concepts Demonstrated

### Flask Application Structure
```python
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

@app.route('/')
def index():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

### Blueprints (Modular Design)
```python
from flask import Blueprint

bp = Blueprint('module_name', __name__)

@bp.route('/example')
def example():
    return 'Module example'

# Register in main app
app.register_blueprint(bp, url_prefix='/prefix')
```

### Database Models
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
```

### Form Validation
```python
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
```

## 🔒 Security Best Practices

This project demonstrates:
- ✅ Password hashing (never store plain passwords)
- ✅ CSRF protection on forms
- ✅ SQL injection prevention (SQLAlchemy ORM)
- ✅ XSS protection (Jinja2 auto-escaping)
- ✅ Secure session management
- ✅ Environment variable configuration

## 🚀 Deployment Tips

When deploying to production:

1. **Set a strong SECRET_KEY**
   ```bash
   python -c 'import secrets; print(secrets.token_hex(16))'
   ```

2. **Disable debug mode**
   ```python
   app.run(debug=False)
   ```

3. **Use a production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

4. **Use PostgreSQL instead of SQLite**
   ```
   DATABASE_URL=postgresql://user:pass@localhost/dbname
   ```

5. **Set proper environment variables**
   - Never commit `.env` to version control
   - Use environment-specific configs

## 📝 Common Tasks

### Create Database Tables
```python
from app import app, db
with app.app_context():
    db.create_all()
```

### Reset Database
```python
with app.app_context():
    db.drop_all()
    db.create_all()
```

### Create Admin User
```python
from modules.auth_module import User
from app import app, db

with app.app_context():
    admin = User(username='admin', email='admin@example.com')
    admin.set_password('secure_password')
    db.session.add(admin)
    db.session.commit()
```

## 🤝 Contributing

This is an educational project. Feel free to:
- Fork and modify for your learning
- Add new modules or examples
- Improve documentation
- Fix bugs

## 📚 Learning Resources

- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/)

## ❓ Troubleshooting

### Port already in use
```bash
# Change the port in app.py
app.run(debug=True, port=5001)
```

### Database locked error
```bash
# Stop the app and delete the database file
rm app.db
# Then restart the app
```

### Module import errors
```bash
# Make sure you're in the project root
uv sync
```

### Missing dependencies
```bash
# Reinstall all dependencies
uv sync --reinstall
```

## 📄 License

This project is open source and available for educational purposes.

## 🎯 Next Steps

After completing this guide, consider:
1. Building your own Flask application
2. Learning about Flask extensions (Flask-Mail, Flask-Cache, etc.)
3. Exploring asynchronous Flask with Quart
4. Learning about containerization with Docker
5. Studying microservices architecture

---

**Happy Learning! 🎉**

Made with ❤️ for Flask beginners
