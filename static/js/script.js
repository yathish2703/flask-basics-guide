// Flask Basics Guide - Main JavaScript

console.log('Flask Basics Guide - JavaScript Loaded');

// Example: Form validation
document.addEventListener('DOMContentLoaded', function() {
    
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.5s';
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
    
    // Confirm before deleting
    const deleteButtons = document.querySelectorAll('[data-confirm]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm(this.getAttribute('data-confirm'))) {
                e.preventDefault();
            }
        });
    });
    
});

// Example function for demos
function showAlert() {
    alert('Hello from Flask Static JavaScript!');
}

// Example function to change colors
function changeColor() {
    const element = document.getElementById('color-demo');
    if (element) {
        const colors = ['#ffcccb', '#90ee90', '#add8e6', '#ffb6c1', '#ffd700'];
        const randomColor = colors[Math.floor(Math.random() * colors.length)];
        element.style.background = randomColor;
    }
}

// API Example Helper
function makeApiRequest(endpoint, method = 'GET', data = null) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        }
    };
    
    if (data) {
        options.body = JSON.stringify(data);
    }
    
    return fetch(endpoint, options)
        .then(response => response.json())
        .then(data => {
            console.log('API Response:', data);
            return data;
        })
        .catch(error => {
            console.error('API Error:', error);
            throw error;
        });
}

// Example: Load tasks from API
function loadTasks() {
    makeApiRequest('/api/tasks')
        .then(data => {
            console.log(`Loaded ${data.count} tasks`);
            // Process tasks here
        });
}
