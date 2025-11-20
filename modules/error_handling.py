"""
Module 7: Error Handling
Learn about custom error pages and error handling in Flask
"""

from flask import Blueprint, render_template, jsonify, request

error_bp = Blueprint('error', __name__)


@error_bp.app_errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    if request.path.startswith('/api/'):
        return jsonify({'error': 'Resource not found', 'status': 404}), 404
    return render_template('errors/404.html'), 404


@error_bp.app_errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    if request.path.startswith('/api/'):
        return jsonify({'error': 'Internal server error', 'status': 500}), 500
    return render_template('errors/500.html'), 500


@error_bp.app_errorhandler(403)
def forbidden_error(error):
    """Handle 403 errors"""
    if request.path.startswith('/api/'):
        return jsonify({'error': 'Forbidden', 'status': 403}), 403
    return render_template('errors/403.html'), 403


@error_bp.route('/trigger-404')
def trigger_404():
    """Route to demonstrate 404 error"""
    from flask import abort
    abort(404)


@error_bp.route('/trigger-500')
def trigger_500():
    """Route to demonstrate 500 error"""
    from flask import abort
    abort(500)


@error_bp.route('/trigger-403')
def trigger_403():
    """Route to demonstrate 403 error"""
    from flask import abort
    abort(403)
