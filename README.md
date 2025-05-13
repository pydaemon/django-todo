# Django To-Do List

A simple To-Do List web application built with Django.  
Users can register, log in, create tasks, mark them as completed, delete tasks, and filter tasks by completion status.

## Features
- User authentication (register, login, logout)
- Create, update, and delete tasks
- Filter tasks by completion status
- Bootstrap for responsive design

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/pydaemon/django-todo.git
   cd django-todo
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the project root and add the following:
   ```
   DEBUG=True
   SECRET_KEY=your-default-secret-key-for-local-dev
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Deployment

Deployed on Render: [https://django-todo-o8k0.onrender.com](https://django-todo-o8k0.onrender.com)

## Technologies Used

- Django 5.2
- Bootstrap 5.3.6
- SQLite  
- Gunicorn  
- python-decouple  
- WhiteNoise
