# NTC PC15 - Python Programming 2 w/ Lab
## Week 9: Introduction to Web Frameworks
### Your Turn: Web Foundation Setup Output

**Institution:** National Teachers College  
**Academic Year:** 2026–2027

### Setup Commands

```bash
python -m venv env
env\Scripts\activate
pip install django
django-admin startproject employee_project
cd employee_project
python manage.py startapp employees
```

### App Registration

Add `'employees'` to `INSTALLED_APPS` in `employee_project/settings.py`.

### Run Development Server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` to confirm the Django default success page.

### Deliverables

- Initialized Django project and app
- App registered in `settings.py`
- Terminal output screenshot
