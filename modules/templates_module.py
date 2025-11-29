"""
Module 2: Templates
Learn about Jinja2 templating, template inheritance, filters, and macros
"""

from flask import Blueprint, render_template

templates_bp = Blueprint('templates', __name__)


@templates_bp.route('/')
def templates_home():
    """Templates module home"""
    return render_template('templates_module/index.html')


@templates_bp.route('/variables')
def variables():
    """Demonstrate template variables"""
    user = {
        'name': 'Yathish',
        'email': 'yathish@gmail.com',
        'age': 25,
        'linkedin_profile': 'https://www.linkedin.com/in/yathish'
    }
    items = ['Python', 'Flask', 'Jinja2', 'SQLAlchemy','VR','AR']
    subtitle = "Learning Flask Templating"
    return render_template('templates_module/variables.html', 
                         user=user, 
                         items=items,
                         subtitle=subtitle,
                         title='Template Variables Demo')


@templates_bp.route('/control-structures')
def control_structures():
    """Demonstrate if statements and loops"""
    users = [
        {'name': 'Alice', 'role': 'Admin', 'active': True},
        {'name': 'Bob', 'role': 'User', 'active': True},
        {'name': 'Charlie', 'role': 'User', 'active': False},
        {'name': 'Diana', 'role': 'Moderator', 'active': True},
    ]
    
    return render_template('templates_module/control_structures.html', 
                         users=users,
                         title='Control Structures Demo')


@templates_bp.route('/filters')
def filters():
    """Demonstrate Jinja2 filters"""
    text = "hello flask world"
    number = 1234567.89
    date_str = "2025-11-20"
    html_text = "<script>alert('xss')</script>"
    items = ['apple', 'banana', 'cherry', 'date']
    
    return render_template('templates_module/filters.html',
                         text=text,
                         number=number,
                         date_str=date_str,
                         html_text=html_text,
                         items=items,
                         title='Filters Demo')


@templates_bp.route('/inheritance')
def inheritance():
    """Demonstrate template inheritance"""
    return render_template('templates_module/child_template.html',
                         title='Template Inheritance',
                         content='This page demonstrates template inheritance!')


@templates_bp.route('/macros')
def macros():
    """Demonstrate macros (reusable template components)"""
    products = [
        {'name': 'Laptop', 'price': 999.99, 'rating': 4.5},
        {'name': 'Mouse', 'price': 29.99, 'rating': 4.0},
        {'name': 'Keyboard', 'price': 79.99, 'rating': 4.8},
    ]
    
    return render_template('templates_module/macros.html',
                         products=products,
                         title='Macros Demo')


@templates_bp.route('/static-demo')
def static_demo():
    """Demonstrate static files (CSS, JS, images)"""
    return render_template('templates_module/static_demo.html',
                         title='Static Files Demo')
