"""
Module 1: Basic Routes
Learn about basic routing, URL parameters, query strings, and HTTP methods
"""

from flask import Blueprint, request, jsonify, render_template

basic_bp = Blueprint('basic', __name__)


@basic_bp.route('/')
def basic_home():
    """Basic route example"""
    return render_template('basic_routes/index.html')


@basic_bp.route('/hello')
def hello():
    """Simple hello route"""
    return render_template('basic_routes/hello.html')


@basic_bp.route('/user/<username>')
def user_profile(username):
    """
    Route with URL parameter
    Example: /basic/user/John will display "Hello, John!"
    """
    return render_template('basic_routes/user_profile.html', username=username)


@basic_bp.route('/user/<int:user_id>/profile')
def user_profile_by_id(user_id):
    """
    Route with typed URL parameter (integer)
    Example: /basic/user/123/profile
    """
    return render_template('basic_routes/user_profile_by_id.html', 
                         user_id=user_id, 
                         type=type(user_id).__name__)


@basic_bp.route('/search')
def search():
    """
    Route demonstrating query string parameters
    Example: /basic/search?q=flask&category=tutorial
    """
    query = request.args.get('q', 'nothing')  # Get 'q' parameter, default 'nothing'
    category = request.args.get('category', 'all')
    page = request.args.get('page', 1, type=int)
    
    return render_template('basic_routes/search.html',
                         query=query,
                         category=category,
                         page=page,
                         all_params=dict(request.args))


@basic_bp.route('/methods-demo', methods=['GET', 'POST', 'PUT', 'DELETE'])
def methods_demo():
    """
    Route demonstrating different HTTP methods
    """
    method = request.method
    
    # Map method to color for UI
    method_colors = {
        'GET': 'blue',
        'POST': 'green',
        'PUT': 'yellow',
        'DELETE': 'red'
    }
    
    if method == 'GET':
        return render_template('basic_routes/methods_demo.html', 
                             method=method,
                             method_color=method_colors.get(method, 'gray'))
    elif method == 'POST':
        return jsonify({'message': 'POST request received', 'method': 'POST'})
    elif method == 'PUT':
        return jsonify({'message': 'PUT request received', 'method': 'PUT'})
    elif method == 'DELETE':
        return jsonify({'message': 'DELETE request received', 'method': 'DELETE'})


@basic_bp.route('/redirect-example')
def redirect_example():
    """Redirect example"""
    from flask import redirect, url_for
    return redirect(url_for('basic.hello'))


@basic_bp.route('/post-only', methods=['POST'])
def post_only():
    """Route that only accepts POST requests"""
    data = request.get_json() if request.is_json else request.form
    return jsonify({'message': 'POST data received', 'data': dict(data)})
