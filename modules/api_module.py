"""
Module 6: API
Learn about creating RESTful APIs with Flask
"""

from flask import Blueprint, jsonify, request
from extensions import db
from modules.database_module import Task
from datetime import datetime

api_bp = Blueprint('api', __name__)


@api_bp.route('/')
def api_home():
    """API module documentation"""
    endpoints = [
        {'method': 'GET', 'path': '/api/tasks', 'description': 'Get all tasks'},
        {'method': 'GET', 'path': '/api/tasks/<id>', 'description': 'Get single task'},
        {'method': 'POST', 'path': '/api/tasks', 'description': 'Create new task'},
        {'method': 'PUT', 'path': '/api/tasks/<id>', 'description': 'Update task'},
        {'method': 'DELETE', 'path': '/api/tasks/<id>', 'description': 'Delete task'},
        {'method': 'GET', 'path': '/api/status', 'description': 'API status'},
    ]
    
    return jsonify({
        'message': 'Flask API Module',
        'version': '1.0',
        'endpoints': endpoints
    })


@api_bp.route('/status')
def status():
    """API status endpoint"""
    return jsonify({
        'status': 'online',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0'
    })


@api_bp.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    tasks = Task.query.all()
    
    return jsonify({
        'count': len(tasks),
        'tasks': [
            {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'priority': task.priority,
                'created_at': task.created_at.isoformat()
            }
            for task in tasks
        ]
    })


@api_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get single task by ID"""
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'priority': task.priority,
        'created_at': task.created_at.isoformat()
    })


@api_bp.route('/tasks', methods=['POST'])
def create_task():
    """Create new task"""
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.get_json()
    
    # Validation
    if not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400
    
    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        priority=data.get('priority', 'medium'),
        completed=data.get('completed', False)
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify({
        'message': 'Task created successfully',
        'task': {
            'id': new_task.id,
            'title': new_task.title,
            'description': new_task.description,
            'completed': new_task.completed,
            'priority': new_task.priority,
            'created_at': new_task.created_at.isoformat()
        }
    }), 201


@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update existing task"""
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.get_json()
    
    # Update fields
    if 'title' in data:
        task.title = data['title']
    if 'description' in data:
        task.description = data['description']
    if 'priority' in data:
        task.priority = data['priority']
    if 'completed' in data:
        task.completed = data['completed']
    
    db.session.commit()
    
    return jsonify({
        'message': 'Task updated successfully',
        'task': {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'completed': task.completed,
            'priority': task.priority,
            'created_at': task.created_at.isoformat()
        }
    })


@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete task"""
    task = Task.query.get(task_id)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({'message': 'Task deleted successfully'}), 200


@api_bp.route('/search', methods=['GET'])
def search_tasks():
    """Search tasks by title"""
    query = request.args.get('q', '')
    
    if not query:
        return jsonify({'error': 'Query parameter "q" is required'}), 400
    
    tasks = Task.query.filter(Task.title.contains(query)).all()
    
    return jsonify({
        'query': query,
        'count': len(tasks),
        'tasks': [
            {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed,
                'priority': task.priority
            }
            for task in tasks
        ]
    })


@api_bp.route('/stats', methods=['GET'])
def get_stats():
    """Get task statistics"""
    total = Task.query.count()
    completed = Task.query.filter_by(completed=True).count()
    pending = total - completed
    
    return jsonify({
        'total_tasks': total,
        'completed': completed,
        'pending': pending,
        'completion_rate': round((completed / total * 100) if total > 0 else 0, 2)
    })
