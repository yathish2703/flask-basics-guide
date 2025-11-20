# Flask Quick Reference Guide

## 🚀 Getting Started

```bash
# Install uv (if not installed)
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell):
# powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip:
# pip install uv

# Install dependencies (creates .venv automatically)
uv sync

# Copy environment file
cp .env.example .env

# Run the application
uv run python app.py

# Visit http://localhost:5000
```

## 📚 Module URLs

| Module | URL | Description |
|--------|-----|-------------|
| Home | `/` | Main landing page |
| Basic Routes | `/basic` | Routing and HTTP methods |
| Templates | `/templates` | Jinja2 templating |
| Forms | `/forms` | Form handling and validation |
| Database | `/database` | SQLAlchemy and CRUD |
| Authentication | `/auth` | User login/registration |
| API | `/api` | RESTful API endpoints |

## 🔑 Common Flask Patterns

### Route with Parameters
```python
@app.route('/user/<username>')
def show_user(username):
    return f'User: {username}'
```

### Render Template
```python
@app.route('/page')
def page():
    return render_template('page.html', title='My Page')
```

### Form Handling
```python
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        data = request.form.get('field')
        return redirect(url_for('success'))
    return render_template('form.html')
```

### Database Query
```python
# Get all
items = Model.query.all()

# Filter
items = Model.query.filter_by(status='active').all()

# Get by ID
item = Model.query.get_or_404(id)

# Create
new_item = Model(name='Example')
db.session.add(new_item)
db.session.commit()

# Update
item.name = 'Updated'
db.session.commit()

# Delete
db.session.delete(item)
db.session.commit()
```

### JSON Response
```python
@app.route('/api/data')
def get_data():
    return jsonify({'key': 'value'})
```

## 🎨 Jinja2 Template Syntax

```jinja2
{# Variable #}
{{ variable }}

{# If statement #}
{% if condition %}
    Content
{% endif %}

{# For loop #}
{% for item in items %}
    {{ item }}
{% endfor %}

{# Template inheritance #}
{% extends "base.html" %}
{% block content %}
    Your content
{% endblock %}

{# Filters #}
{{ text|upper }}
{{ number|round(2) }}
{{ items|length }}
```

## 🔐 Authentication

```python
# Login user
login_user(user, remember=True)

# Logout
logout_user()

# Protected route
@login_required
def protected():
    return f'Hello {current_user.username}'

# Check if authenticated
if current_user.is_authenticated:
    # User is logged in
```

## 🛠️ Useful Commands

```bash
# Create database
uv run python -c "from app import app, db; app.app_context().push(); db.create_all()"

# Reset database
uv run python -c "from app import app, db; app.app_context().push(); db.drop_all(); db.create_all()"

# Generate secret key
uv run python -c "import secrets; print(secrets.token_hex(16))"

# Add new package
uv add package-name

# Remove package
uv remove package-name

# Update packages
uv sync --upgrade
```

## 📦 Project Structure Reference

```
flask-basics-guide/
├── app.py              # Main application
├── pyproject.toml      # Dependencies (uv)
├── uv.lock            # Lock file
├── .env               # Environment variables (create from .env.example)
├── modules/           # Blueprint modules
│   ├── basic_routes.py
│   ├── templates_module.py
│   ├── forms_module.py
│   ├── database_module.py
│   ├── auth_module.py
│   ├── api_module.py
│   └── error_handling.py
├── templates/         # HTML templates
│   ├── base.html
│   ├── index.html
│   └── [module folders]
└── static/           # CSS, JS, images
    ├── css/style.css
    └── js/script.js
```

## 🐛 Debugging Tips

1. **Enable debug mode**: `app.run(debug=True)`
2. **Check logs**: Look at terminal output
3. **Use print/logging**: Add print statements
4. **Test in isolation**: Test one function at a time
5. **Check database**: Verify data is being saved

## 📖 Learn More

- Each module has extensive code comments
- Visit each URL to see live examples
- Check the README.md for detailed explanations
- Experiment by modifying the code!

---

**Happy Flask Development! 🎉**
