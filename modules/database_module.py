"""
Module 4: Database Operations with SQLAlchemy ORM

What is ORM (Object-Relational Mapping)?
- ORM converts Python objects into database tables automatically
- Write Python code instead of SQL queries
- Each class = database table, each object = row in table
- SQLAlchemy is Flask's most popular ORM library

Benefits:
✓ Write database code in Python (no SQL needed)
✓ Database-agnostic (works with SQLite, PostgreSQL, MySQL, etc.)
✓ Prevents SQL injection attacks automatically
✓ Easy to maintain and refactor
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db  # Import SQLAlchemy instance
from datetime import datetime

database_bp = Blueprint('database', __name__)


# ============================================================================
# DATABASE MODELS (ORM Classes)
# ============================================================================
# Each class represents a table in the database
# Each attribute represents a column in that table

class Task(db.Model):
    """
    Task Model - Represents 'task' table in database
    
    ORM Concept: This class definition automatically creates a table named 'task'
    with columns matching the attributes below.
    
    SQL Equivalent:
    CREATE TABLE task (
        id INTEGER PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        description TEXT,
        completed BOOLEAN DEFAULT FALSE,
        priority VARCHAR(20) DEFAULT 'medium',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    # Primary Key - Unique identifier for each task (auto-increments)
    id = db.Column(db.Integer, primary_key=True)
    # primary_key=True means: this column uniquely identifies each row
    # db.Integer means: store whole numbers (1, 2, 3...)
    
    # Title field - Required text up to 100 characters
    title = db.Column(db.String(100), nullable=False)
    # db.String(100) = VARCHAR(100) in SQL - text with max 100 chars
    # nullable=False means this field is REQUIRED (can't be empty)
    
    # Description field - Optional longer text
    description = db.Column(db.Text, nullable=True)
    # db.Text = unlimited text length (like TEXT in SQL)
    # nullable=True means OPTIONAL (can be empty)
    
    # Completed status - True/False flag
    completed = db.Column(db.Boolean, default=False)
    # db.Boolean = True or False (1 or 0 in database)
    # default=False means new tasks start as incomplete
    
    # Priority level - low, medium, or high
    priority = db.Column(db.String(20), default='medium')
    # default='medium' sets initial value if not provided
    
    # Timestamp - When task was created
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # db.DateTime stores date and time
    # default=datetime.utcnow automatically sets current time when created
    # Note: Use utcnow (not utcnow()) to pass function reference
    
    def __repr__(self):
        """
        String representation of Task object (for debugging)
        When you print(task), you'll see: <Task Learn Flask>
        """
        return f'<Task {self.title}>'


class Category(db.Model):
    """
    Category Model - Demonstrates how to create additional tables
    
    In a real app, you might link tasks to categories using relationships.
    This shows the basic structure of a second model.
    """
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Unique constraint prevents duplicate category names
    name = db.Column(db.String(50), nullable=False, unique=True)
    # unique=True means: no two categories can have the same name
    
    description = db.Column(db.String(200))
    
    def __repr__(self):
        return f'<Category {self.name}>'


# ============================================================================
# ROUTES - CRUD OPERATIONS
# ============================================================================

@database_bp.route('/')
def database_home():
    """Database module home page with ORM overview"""
    return render_template('database_module/index.html')


@database_bp.route('/tasks')
def tasks():
    """
    READ Operation - Display all tasks
    
    ORM Query Explanation:
    - Task.query.all() → SELECT * FROM task
    - Returns list of Task objects (not raw SQL results)
    - Each object has attributes: task.title, task.completed, etc.
    """
    # Query all tasks from database using ORM
    all_tasks = Task.query.all()
    # This is equivalent to: SELECT * FROM task;
    # Returns: [<Task 1>, <Task 2>, <Task 3>...]
    
    return render_template('database_module/tasks.html', tasks=all_tasks)


@database_bp.route('/tasks/create', methods=['GET', 'POST'])
def create_task():
    """
    CREATE Operation - Add new task to database
    
    ORM Steps:
    1. Create Python object: new_task = Task(...)
    2. Add to session: db.session.add(new_task)
    3. Commit to database: db.session.commit()
    
    Why this approach?
    - Session acts as a "staging area" for changes
    - Multiple changes can be grouped together
    - commit() saves all changes at once (atomic transaction)
    """
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        description = request.form.get('description')
        priority = request.form.get('priority', 'medium')
        
        # Validation
        if not title:
            flash('Title is required!', 'error')
            return redirect(url_for('database.create_task'))
        
        # Step 1: Create new Task object (Python object, not in DB yet)
        new_task = Task(
            title=title,
            description=description,
            priority=priority
        )
        # At this point: object exists in memory only
        
        # Step 2: Add to database session (staging)
        db.session.add(new_task)
        # Still not in database - just marked for insertion
        
        # Step 3: Commit - actually save to database
        db.session.commit()
        # NOW it's saved! SQL: INSERT INTO task VALUES (...)
        # new_task.id is automatically set by database
        
        flash('Task created successfully!', 'success')
        return redirect(url_for('database.tasks'))
    
    # GET request - show the form
    return render_template('database_module/create_task.html')


@database_bp.route('/tasks/<int:task_id>')
def view_task(task_id):
    """
    READ Single Record - Get one specific task
    
    ORM Methods:
    - get_or_404(id) → Find by primary key or show 404 error
    - SQL: SELECT * FROM task WHERE id = ?
    """
    # Find task by ID, or return 404 error if not found
    task = Task.query.get_or_404(task_id)
    # Equivalent: SELECT * FROM task WHERE id = task_id LIMIT 1
    # If not found: automatically returns "404 Not Found" error page
    
    return render_template('database_module/view_task.html', task=task)


@database_bp.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    """
    UPDATE Operation - Modify existing task
    
    ORM Pattern:
    1. Query the object: task = Task.query.get_or_404(id)
    2. Modify attributes: task.title = "New Title"
    3. Commit changes: db.session.commit()
    
    Why so simple?
    - SQLAlchemy tracks changes automatically
    - Just modify object attributes, then commit
    - No need to write UPDATE query manually
    """
    # Get the task to edit
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'POST':
        # Update task attributes directly
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        task.priority = request.form.get('priority', 'medium')
        task.completed = 'completed' in request.form  # Checkbox handling
        
        # SQLAlchemy detects these changes automatically!
        # Just commit to save
        db.session.commit()
        # SQL: UPDATE task SET title=?, description=?, priority=?, completed=? WHERE id=?
        
        flash('Task updated successfully!', 'success')
        return redirect(url_for('database.tasks'))
    
    # GET request - show edit form with current values
    return render_template('database_module/edit_task.html', task=task)


@database_bp.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    """
    DELETE Operation - Remove task from database
    
    ORM Steps:
    1. Find the object: task = Task.query.get_or_404(id)
    2. Delete it: db.session.delete(task)
    3. Commit: db.session.commit()
    """
    # Find the task
    task = Task.query.get_or_404(task_id)
    
    # Mark for deletion
    db.session.delete(task)
    # Not deleted yet - just staged for deletion
    
    # Execute the deletion
    db.session.commit()
    # SQL: DELETE FROM task WHERE id = ?
    
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('database.tasks'))


@database_bp.route('/tasks/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    """
    UPDATE Operation - Toggle boolean field
    
    Common Pattern:
    - Flip boolean: task.completed = not task.completed
    - Update timestamps: task.updated_at = datetime.utcnow()
    - Increment counters: task.view_count += 1
    """
    task = Task.query.get_or_404(task_id)
    
    # Flip the completed status (True → False, or False → True)
    task.completed = not task.completed
    
    # Commit the change
    db.session.commit()
    # SQL: UPDATE task SET completed = ? WHERE id = ?
    
    status = 'completed' if task.completed else 'reopened'
    flash(f'Task {status}!', 'success')
    return redirect(url_for('database.tasks'))


@database_bp.route('/queries')
def queries():
    """
    Advanced ORM Queries - Different ways to query data
    
    Common Query Methods:
    =====================
    .all()          → Get all records (returns list)
    .first()        → Get first record (returns object or None)
    .get(id)        → Get by primary key
    .filter_by()    → Simple filtering (column=value)
    .filter()       → Complex filtering (with operators)
    .order_by()     → Sort results
    .limit()        → Limit number of results
    .count()        → Count records
    
    Query Chaining:
    ===============
    You can chain methods:
    Task.query.filter_by(completed=True).order_by(Task.created_at.desc()).limit(5).all()
    """
    
    # 1. Get ALL tasks
    all_tasks = Task.query.all()
    # SQL: SELECT * FROM task
    # Returns: list of all Task objects
    
    # 2. Get FIRST task (or None if table is empty)
    first_task = Task.query.first()
    # SQL: SELECT * FROM task LIMIT 1
    # Returns: single Task object or None
    
    # 3. Filter by specific value
    completed_tasks = Task.query.filter_by(completed=True).all()
    # SQL: SELECT * FROM task WHERE completed = TRUE
    # .filter_by() is simple: column_name=value
    
    # 4. Filter by another value
    high_priority = Task.query.filter_by(priority='high').all()
    # SQL: SELECT * FROM task WHERE priority = 'high'
    
    # 5. Order results (sort)
    ordered_tasks = Task.query.order_by(Task.created_at.desc()).all()
    # SQL: SELECT * FROM task ORDER BY created_at DESC
    # .desc() = descending (newest first)
    # .asc() = ascending (oldest first)
    
    # 6. Limit results
    limited_tasks = Task.query.limit(5).all()
    # SQL: SELECT * FROM task LIMIT 5
    # Get only first 5 records
    
    # 7. Count records (without loading all data)
    task_count = Task.query.count()
    # SQL: SELECT COUNT(*) FROM task
    # More efficient than len(Task.query.all())
    
    # 8. Complex filtering with .filter()
    # recent_high_priority = Task.query.filter(
    #     Task.priority == 'high',
    #     Task.created_at > datetime.utcnow() - timedelta(days=7)
    # ).all()
    # Use .filter() for operators: ==, !=, >, <, >=, <=
    
    # 9. Chaining multiple methods
    recent_incomplete = Task.query.filter_by(
        completed=False
    ).order_by(
        Task.created_at.desc()
    ).limit(10).all()
    # SQL: SELECT * FROM task WHERE completed = FALSE 
    #      ORDER BY created_at DESC LIMIT 10
    
    # Prepare results for template
    query_results = {
        'total_tasks': len(all_tasks),
        'completed_count': len(completed_tasks),
        'high_priority_count': len(high_priority),
        'first_task': first_task,
        'recent_tasks': limited_tasks,
        'task_count': task_count
    }
    
    return render_template('database_module/queries.html', results=query_results)


# ============================================================================
# COMMON ORM PATTERNS & BEST PRACTICES
# ============================================================================
"""
Pattern 1: Create and Save
---------------------------
obj = Model(field1=value1, field2=value2)
db.session.add(obj)
db.session.commit()

Pattern 2: Query and Update
----------------------------
obj = Model.query.get(id)
obj.field = new_value
db.session.commit()  # No need to add() again!

Pattern 3: Query and Delete
----------------------------
obj = Model.query.get(id)
db.session.delete(obj)
db.session.commit()

Pattern 4: Bulk Operations
---------------------------
# Update multiple records
Task.query.filter_by(completed=True).update({'priority': 'low'})
db.session.commit()

# Delete multiple records
Task.query.filter_by(priority='low').delete()
db.session.commit()

Error Handling:
---------------
try:
    db.session.commit()
except Exception as e:
    db.session.rollback()  # Undo changes if error occurs
    print(f"Error: {e}")

Session Management:
-------------------
- db.session tracks all changes
- commit() saves all changes at once
- rollback() cancels all pending changes
- flush() sends changes to DB but doesn't commit (advanced)

Best Practices:
---------------
✓ Always commit() after modifications
✓ Use get_or_404() for single record lookups
✓ Use filter_by() for simple filters
✓ Use filter() for complex conditions
✓ Add indexes on frequently queried columns
✓ Use .count() instead of len(.all()) for counting
✓ Handle exceptions with try/except and rollback()
"""
