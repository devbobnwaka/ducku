# ducku
Ducku is a web-based documentation tool for businesses.
Its goal is to make it easier for employees and/or others to share knowledge within a company!!!
The objective of this application is to learn how to establish authentication and permissions for different kinds of users in Django.

# How the application works.
- An organization will register completing the registration form

## When an organational user is authenticated

- An organization can create/add departments/sections
- An organization can create users within it organization.
- Organization user can create a new user by completing the register member form.

# For Registered members
- Users or members can login using credentials created by the organization
- Create, Edit, VIew, Delete an Article
- Logout


# TO TEST THE APPLICATION

## Getting Started

1. Create virtual environment

```bash
#for windows
python -m venv .venv
```

2. Activate virtual environment
```bash
#for windows
.venv\Scripts\activate
```

3. Install all dependencies
```bash
#for windows
pip install -r requirements.txt
```

4. Run the Migrations
Current setup is for POSTGRES_DB, to use SQLite, uncomment the django.db.backends.sqlite3 Database setting and comment the POSTGRES_DB settings
```bash
#for windows
python manage.py makemigrations
python manage.py migrate
``` 

5. Run the development server
```bash
#for windows
python manage.py runserver
```

