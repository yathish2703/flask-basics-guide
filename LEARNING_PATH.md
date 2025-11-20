# 🎓 Learning Path & Exercises

This guide provides a structured learning path and hands-on exercises for each module.

## 📖 Recommended Learning Order

### Week 1: Basics
1. ✅ **Module 1: Basic Routes** (Day 1-2)
   - Understand how routing works
   - Practice with URL parameters
   - Learn HTTP methods
   
2. ✅ **Module 2: Templates** (Day 3-4)
   - Master Jinja2 syntax
   - Create reusable layouts
   - Use filters and macros

### Week 2: Data Handling
3. ✅ **Module 3: Forms** (Day 5-6)
   - Build and validate forms
   - Implement CSRF protection
   - Handle file uploads

4. ✅ **Module 4: Database** (Day 7-8)
   - Create database models
   - Perform CRUD operations
   - Write complex queries

### Week 3: Advanced Features
5. ✅ **Module 5: Authentication** (Day 9-10)
   - Implement user registration
   - Secure password storage
   - Manage sessions

6. ✅ **Module 6: API** (Day 11-12)
   - Build RESTful endpoints
   - Return JSON responses
   - Handle HTTP status codes

### Week 4: Polish
7. ✅ **Module 7: Error Handling** (Day 13)
   - Custom error pages
   - Graceful error handling

8. ✅ **Final Project** (Day 14)
   - Combine all concepts
   - Build your own app

## 💡 Practice Exercises

### Module 1: Basic Routes

**Exercise 1: Calculator Routes**
Create routes that perform calculations:
```python
# /add/5/3 should return 8
# /multiply/4/7 should return 28
```

**Exercise 2: Blog Post Route**
Create a route that displays blog posts:
```python
# /blog/post/my-first-post
# /blog/2025/11/20
```

**Exercise 3: Search Function**
Build a search route that accepts multiple parameters:
```python
# /search?q=flask&category=python&sort=date
```

---

### Module 2: Templates

**Exercise 1: Product Catalog**
Create a template that displays products in a grid with:
- Product name, price, image
- Filter by category
- Sort by price

**Exercise 2: Blog Template**
Build a blog template with:
- Post list page
- Individual post page
- Sidebar with recent posts
- Template inheritance

**Exercise 3: Dashboard**
Create a dashboard template showing:
- Statistics cards
- Data charts
- Recent activity feed

---

### Module 3: Forms

**Exercise 1: Contact Form**
Build a contact form with:
- Name, email, subject, message
- Validation for all fields
- Email format validation
- Success message

**Exercise 2: Profile Update Form**
Create a profile form with:
- Username, bio, avatar upload
- Date picker for birthday
- Country dropdown
- Save changes

**Exercise 3: Multi-Step Form**
Build a registration wizard:
- Step 1: Basic info
- Step 2: Address
- Step 3: Preferences
- Step 4: Review & submit

---

### Module 4: Database

**Exercise 1: Blog System**
Create a complete blog with:
- Post model (title, content, author, date)
- Category model
- CRUD operations
- Relationship between posts and categories

**Exercise 2: Todo App**
Build a todo application:
- Task model with priority and due date
- Mark tasks as complete
- Filter by status
- Sort by priority

**Exercise 3: Inventory System**
Create an inventory tracker:
- Product model
- Track quantity, price, supplier
- Low stock alerts
- Search and filter products

---

### Module 5: Authentication

**Exercise 1: Role-Based Access**
Add user roles:
- Admin, Moderator, User roles
- Different permissions for each
- Protect routes based on role

**Exercise 2: Profile Management**
Add profile features:
- Edit profile information
- Change password
- Upload profile picture
- View user activity

**Exercise 3: Password Reset**
Implement password reset:
- "Forgot password" link
- Email with reset token
- Reset password form
- Security measures

---

### Module 6: API

**Exercise 1: Full CRUD API**
Create a complete REST API for books:
```
GET    /api/books          # List all
GET    /api/books/1        # Get one
POST   /api/books          # Create
PUT    /api/books/1        # Update
DELETE /api/books/1        # Delete
```

**Exercise 2: API with Pagination**
Add pagination to your API:
```
GET /api/books?page=2&per_page=10
```

**Exercise 3: API Authentication**
Secure your API:
- API key authentication
- Rate limiting
- Token-based auth

---

### Module 7: Error Handling

**Exercise 1: Custom Error Pages**
Design beautiful error pages:
- 404 with helpful suggestions
- 500 with contact information
- 403 with login prompt

**Exercise 2: Error Logging**
Implement error logging:
- Log errors to file
- Email admin on critical errors
- Display friendly messages to users

---

## 🏆 Final Project Ideas

### 1. Blog Platform
- User registration and authentication
- Create, edit, delete posts
- Categories and tags
- Comments system
- Search functionality
- Admin dashboard

### 2. Task Management App
- User accounts
- Create projects and tasks
- Assign tasks to users
- Set priorities and due dates
- Filter and search
- Email notifications

### 3. E-commerce Store
- Product catalog
- Shopping cart
- User accounts
- Order management
- Admin panel
- Payment integration (simulation)

### 4. Social Media Clone
- User profiles
- Posts and comments
- Follow/unfollow users
- Like and share
- Timeline feed
- Notifications

### 5. Recipe Sharing Platform
- Recipe database
- User-submitted recipes
- Rating and reviews
- Search by ingredients
- Save favorites
- Shopping list generator

## 📝 Code Challenge: Build a Feature

Pick one and implement it:

1. **Add search to the task manager**
   - Search by title and description
   - Filter by priority and status
   - Sort results

2. **Create a user profile page**
   - Display user information
   - Show user's tasks
   - Edit profile functionality

3. **Implement tags for tasks**
   - Many-to-many relationship
   - Add/remove tags
   - Filter tasks by tag

4. **Add comments to tasks**
   - Comment model
   - Display comments
   - Delete comments

5. **Create an activity log**
   - Track user actions
   - Display recent activity
   - Filter by action type

## 🎯 Assessment Checklist

After completing each module, check if you can:

### Module 1: Routes
- [ ] Create basic routes
- [ ] Use URL parameters
- [ ] Handle different HTTP methods
- [ ] Redirect users
- [ ] Access query parameters

### Module 2: Templates
- [ ] Pass data to templates
- [ ] Use control structures
- [ ] Apply filters
- [ ] Create template inheritance
- [ ] Build macros

### Module 3: Forms
- [ ] Create HTML forms
- [ ] Use Flask-WTF
- [ ] Validate form data
- [ ] Display error messages
- [ ] Handle file uploads

### Module 4: Database
- [ ] Define models
- [ ] Perform CRUD operations
- [ ] Write queries
- [ ] Filter and sort data
- [ ] Create relationships

### Module 5: Authentication
- [ ] Register users
- [ ] Hash passwords securely
- [ ] Login/logout
- [ ] Protect routes
- [ ] Access current user

### Module 6: API
- [ ] Create JSON endpoints
- [ ] Handle different HTTP methods
- [ ] Return proper status codes
- [ ] Parse JSON requests
- [ ] Document API

### Module 7: Errors
- [ ] Create custom error pages
- [ ] Handle different error types
- [ ] Log errors properly
- [ ] Display user-friendly messages

## 🚀 Next Steps

After mastering these modules:

1. **Learn Flask Extensions**
   - Flask-Mail (email sending)
   - Flask-Cache (caching)
   - Flask-Admin (admin interface)
   - Flask-RESTful (advanced API)

2. **Study Advanced Topics**
   - Testing (pytest, unittest)
   - Deployment (Heroku, AWS, Docker)
   - Async Flask (Quart)
   - WebSockets (Flask-SocketIO)

3. **Build Your Own Project**
   - Start from scratch
   - Apply all concepts learned
   - Deploy to production
   - Share with the community

4. **Contribute to Open Source**
   - Find Flask projects on GitHub
   - Submit bug fixes
   - Add features
   - Improve documentation

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Real Python Flask Tutorials](https://realpython.com/tutorials/flask/)
- [Miguel Grinberg's Blog](https://blog.miguelgrinberg.com/)
- [Full Stack Python](https://www.fullstackpython.com/flask.html)
- [Awesome Flask](https://github.com/mjhea0/awesome-flask)

---

**Keep Learning and Building! 💪**
