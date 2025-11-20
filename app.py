"""
Flask Basics Guide - Main Application
A comprehensive starter guide for Flask beginners with modular examples
"""

from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
from extensions import db, login_manager
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Import and register blueprints
from modules.basic_routes import basic_bp
from modules.templates_module import templates_bp
from modules.forms_module import forms_bp
from modules.database_module import database_bp
from modules.auth_module import auth_bp, load_user  # Import load_user to register it
from modules.api_module import api_bp
from modules.error_handling import error_bp

app.register_blueprint(basic_bp, url_prefix='/basic')
app.register_blueprint(templates_bp, url_prefix='/templates')
app.register_blueprint(forms_bp, url_prefix='/forms')
app.register_blueprint(database_bp, url_prefix='/database')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(error_bp)


@app.route('/')
def index():
    """Home page with links to all modules"""
    learning_resources = [
        {
            'name': 'Why Flask?',
            'url': '/why-flask',
            'description': 'Discover Flask advantages, key concepts, and multiple examples',
            'icon': '💡'
        },
        {
            'name': 'How Web Works',
            'url': '/how-web-works',
            'description': 'Learn how websites work from URL to rendered page',
            'icon': '🌐'
        },
        {
            'name': 'REST Protocol',
            'url': '/rest-protocol',
            'description': 'Understand REST API with fun examples and games!',
            'icon': '🔄'
        },
        {
            'name': 'Routes Explained',
            'url': '/routes-explained',
            'description': 'Learn routes with real-world examples: State → City → Area → Factory',
            'icon': '🗺️'
        },
        {
            'name': 'Learning Games',
            'url': '/games',
            'description': 'Interactive games to learn web concepts: Web Server, REST API, Routes',
            'icon': '🎮'
        }
    ]
    
    flask_modules = [
        {
            'name': 'Basic Routes',
            'url': '/basic',
            'description': 'Learn basic routing, URL parameters, and HTTP methods',
            'icon': '🛣️'
        },
        {
            'name': 'Templates',
            'url': '/templates',
            'description': 'Jinja2 templating, template inheritance, and filters',
            'icon': '📄'
        },
        {
            'name': 'Forms',
            'url': '/forms',
            'description': 'Form handling, validation, and Flask-WTF integration',
            'icon': '📝'
        },
        {
            'name': 'Database',
            'url': '/database',
            'description': 'SQLAlchemy models and CRUD operations',
            'icon': '🗄️'
        },
        {
            'name': 'Authentication',
            'url': '/auth',
            'description': 'User registration, login, and session management',
            'icon': '🔐'
        },
        {
            'name': 'API',
            'url': '/api',
            'description': 'RESTful API creation with JSON responses',
            'icon': '🔌'
        },
        {
            'name': 'Static Files',
            'url': '/templates/static-demo',
            'description': 'CSS, JavaScript, and static file serving',
            'icon': '📦'
        }
    ]
    return render_template('index.html', learning_resources=learning_resources, flask_modules=flask_modules)

# Why Flask? explanation page
@app.route('/why-flask')
def why_flask():
    """Page explaining Flask's advantages and examples"""
    return render_template('why_flask.html')

# How Web Works explanation page
@app.route('/how-web-works')
def how_web_works():
    """Page explaining how web pages work"""
    return render_template('how_web_works.html')

# REST Protocol explanation page
@app.route('/rest-protocol')
def rest_protocol():
    """Kid-friendly explanation of REST API"""
    return render_template('rest_protocol.html')

# Routes explanation page
@app.route('/routes-explained')
def routes_explained():
    """Comprehensive explanation of routes with real-world examples"""
    return render_template('routes_explained.html')

# Games Hub
@app.route('/games')
def games_hub():
    """Hub page for all learning games"""
    return render_template('games_hub.html')

@app.route('/games/web-server')
def game_web_server():
    """Web server learning game"""
    return render_template('game_web_server.html')

@app.route('/games/rest-protocol')
def game_rest_protocol():
    """REST protocol learning game"""
    return render_template('game_rest_protocol.html')

@app.route('/games/routes-builder')
def game_routes_builder():
    """Routes builder learning game"""
    return render_template('game_routes_builder.html')

@app.route('/games/master-challenge')
def game_master_challenge():
    """Master challenge combining all concepts"""
    return render_template('game_master_challenge.html')

@app.route('/games/quick-practice')
def game_quick_practice():
    """Quick practice mini-games"""
    return render_template('game_quick_practice.html')

@app.route('/games/learning-path')
def game_learning_path():
    """Guided learning path with progress tracking"""
    return render_template('game_learning_path.html')

# Real-world hierarchical routing examples
@app.route('/india/<state>')
def state_info(state):
    """Show information about a state"""
    states_data = {
        'karnataka': {'name': 'Karnataka', 'capital': 'Bengaluru', 'population': '68.4M'},
        'tamilnadu': {'name': 'Tamil Nadu', 'capital': 'Chennai', 'population': '77.8M'},
        'kerala': {'name': 'Kerala', 'capital': 'Thiruvananthapuram', 'population': '35.7M'},
        'telangana': {'name': 'Telangana', 'capital': 'Hyderabad', 'population': '39.1M'},
        'andhrapradesh': {'name': 'Andhra Pradesh', 'capital': 'Amaravati', 'population': '52.2M'}
    }
    
    # Cities data organized by state
    state_cities = {
        'karnataka': ['bengaluru', 'mysuru', 'mangaluru', 'hubballi'],
        'tamilnadu': ['chennai', 'coimbatore'],
        'kerala': ['kochi', 'trivandrum'],
        'telangana': ['hyderabad'],
        'andhrapradesh': ['vijayawada', 'visakhapatnam']
    }
    
    state_normalized = state.lower().replace(' ', '')
    state_info = states_data.get(state_normalized, {'name': state, 'capital': 'Unknown', 'population': 'Unknown'})
    available_cities = state_cities.get(state_normalized, [])
    
    return render_template('state_info.html', state=state_info, available_cities=available_cities)

@app.route('/india/<state>/<city>')
def city_info(state, city):
    """Show information about a city in a state"""
    cities_data = {
        'karnataka': {
            'bengaluru': {'name': 'Bengaluru', 'population': '12.8M', 'area': '741 sq km'},
            'mysuru': {'name': 'Mysuru', 'population': '1.2M', 'area': '155 sq km'},
            'mangaluru': {'name': 'Mangaluru', 'population': '0.7M', 'area': '184 sq km'},
            'hubballi': {'name': 'Hubballi', 'population': '1.0M', 'area': '213 sq km'}
        },
        'tamilnadu': {
            'chennai': {'name': 'Chennai', 'population': '11.5M', 'area': '426 sq km'},
            'coimbatore': {'name': 'Coimbatore', 'population': '2.6M', 'area': '246 sq km'}
        },
        'kerala': {
            'kochi': {'name': 'Kochi', 'population': '2.1M', 'area': '94 sq km'},
            'trivandrum': {'name': 'Thiruvananthapuram', 'population': '1.7M', 'area': '214 sq km'}
        },
        'telangana': {
            'hyderabad': {'name': 'Hyderabad', 'population': '10.3M', 'area': '650 sq km'}
        },
        'andhrapradesh': {
            'vijayawada': {'name': 'Vijayawada', 'population': '2.5M', 'area': '261 sq km'},
            'visakhapatnam': {'name': 'Visakhapatnam', 'population': '2.2M', 'area': '681 sq km'}
        }
    }
    state_normalized = state.lower().replace(' ', '')
    state_cities = cities_data.get(state_normalized, {})
    city_info = state_cities.get(city.lower(), {'name': city, 'population': 'Unknown', 'area': 'Unknown'})
    
    # Get list of available cities for this state
    available_cities = [{'id': city_id, 'name': city_data['name']} 
                       for city_id, city_data in state_cities.items()]
    
    return render_template('city_info.html', state=state, city=city_info, available_cities=available_cities)

@app.route('/india/<state>/<city>/<area>')
def area_info(state, city, area):
    """Show information about an area in a city"""
    areas_data = {
        'peenya': {'name': 'Peenya Industrial Area', 'type': 'Manufacturing Hub', 'pin': '560058'},
        'whitefield': {'name': 'Whitefield', 'type': 'IT Corridor', 'pin': '560066'},
        'koramangala': {'name': 'Koramangala', 'type': 'Startup Hub', 'pin': '560034'},
        'majestic': {'name': 'Majestic', 'type': 'Commercial Center', 'pin': '560009'},
        'electronic-city': {'name': 'Electronic City', 'type': 'IT Park', 'pin': '560100'},
        'jayanagar': {'name': 'Jayanagar', 'type': 'Residential', 'pin': '560041'}
    }
    area_info = areas_data.get(area.lower(), {'name': area, 'type': 'Unknown', 'pin': 'Unknown'})
    return render_template('area_info.html', state=state, city=city, area=area_info)

@app.route('/india/<state>/<city>/<area>/<factory>')
def factory_info(state, city, area, factory):
    """Show information about a factory in an area"""
    factories_data = {
        'infosys': {
            'name': 'Infosys Limited',
            'type': 'IT Services',
            'employees': 15000,
            'products': ['Software Development', 'Cloud Services', 'AI Solutions'],
            'established': 1981
        },
        'bosch': {
            'name': 'Bosch India',
            'type': 'Automotive & Technology',
            'employees': 8000,
            'products': ['Auto Parts', 'Power Tools', 'Home Appliances'],
            'established': 1951
        },
        'biocon': {
            'name': 'Biocon Biologics',
            'type': 'Pharmaceuticals',
            'employees': 5000,
            'products': ['Biosimilars', 'Insulin', 'Vaccines'],
            'established': 1978
        },
        'toyota': {
            'name': 'Toyota Kirloskar Motor',
            'type': 'Automobile Manufacturing',
            'employees': 6500,
            'products': ['Innova', 'Fortuner', 'Camry'],
            'established': 1997
        },
        'wipro': {
            'name': 'Wipro Technologies',
            'type': 'IT Services',
            'employees': 12000,
            'products': ['Software', 'Consulting', 'Digital Services'],
            'established': 1945
        }
    }
    factory_info = factories_data.get(factory.lower(), 
                                      {'name': factory, 'type': 'Unknown', 'employees': 0, 
                                       'products': [], 'established': 'Unknown'})
    return render_template('factory_info.html', state=state, city=city, area=area, factory=factory_info)


# Create database tables
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
