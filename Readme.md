# To-Do API

A simple To-Do application built with Django Rest Framework (DRF). This application allows users to manage tasks through a RESTful API. Users can create, retrieve, update, and delete tasks. The project is designed with clean, modular code and follows best practices for API development.

---

## Features

- Add a new To-Do task.
- Retrieve a list of all To-Do tasks.
- Retrieve, update, or delete a specific To-Do task.
- Delete all tasks (optional feature).
- Includes automated test cases for all API endpoints.
- Utilizes SQLite (default) or PostgreSQL database.

---

## Tech Stack

- **Backend**: Django Rest Framework
- **Database**: SQLite (default for testing) or PostgreSQL
- **Testing**: Django's APITestCase

---

## Requirements

Make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Git
- PostgreSQL (if using a remote database)

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd <project_directory>

Here’s the complete **setup section** with the additional content included, written in Markdown format:

---

```markdown
## Setup Instructions

1. **Clone the Repository**
   Clone the project from the repository:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Create and Activate a Virtual Environment**
   Set up a virtual environment to isolate project dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages**
   Install Django, Django Rest Framework, and all other dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   The project uses SQLite as the default database for testing purposes.

   For deployment, the project is configured to use PostgreSQL as the database backend. If you prefer to use PostgreSQL locally:  

   If you prefer to use PostgreSQL Locally:
   - Update the `DATABASES` setting in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_database_user',
             'PASSWORD': 'your_database_password',
             'HOST': 'your_database_host',
             'PORT': '5432',
         }
     }
     ```
   - Ensure PostgreSQL is installed and running, and the database is created.

5. **Apply Database Migrations**
   Apply migrations to create the necessary tables:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**
   Start the server to access the application:
   ```bash
   python manage.py runserver
   ```
   The API will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).


## API Endpoints

The following endpoints are available:

### **Task List**
- **GET /tasks/**: Retrieve a list of all tasks.
- **POST /tasks/**: Create a new task.

### **Task Detail**
- **GET /tasks/<id>/**: Retrieve a specific task by ID.
- **PUT /tasks/<id>/**: Update a specific task by ID.
- **DELETE /tasks/<id>/**: Delete a specific task by ID.

Use the test suite or Postman to verify each endpoint's functionality.

```

---


