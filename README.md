Project structure
minidjango_ver1
    - app1
        - migrations #package
            - __init__.py
        - __init__.py
        - admin.py
        - apps.py
        - models.py
        - tests.py
        - views.py
    - minidjango_ver1
        - __init__.py
        - asgi.py
        - settings.py
        - urls.py
        - wsgi.py
    - venv
        - db.sqlite3
        - manage.py
        - README.md
STEPs
1. create venv 
2. activate venv 
3. pip install django 
4. django-admin (CLI tool options - django-admin --help)
5. django-admin startproject <project-name>
6. Skeleton of project structure because of django-admin startproject command

- Easier steps to get started with Django
1. Install django globally (system-wide installation pip install django)
2. django-admin startproject minidjango_ver1 
3. Open the project minidjango_ver1 in Pycharm 
4. Create a venv under project root (minidjango_ver1)
5. Active venv and pip install django 
6. Write down project structure manually 
7. minidjango_ver1  (django project root)
    - manage.py 
    - minidjango_ver1  (django project setting directory)
         - __init__.py
         - wsgi.py
         - settings.py
         - urls.py 
8. Navigate to django project root (where manage.py file exists)
9. python manage.py startapp app1 (django-admin startapp app1)
10. Write down project structure manually 
11. Register newly created application in settings.py. To register add application name to the existing list called INSTALLED_APPS 
12. Write a first hello_world view inside minidjango_ver1/app1/views.py 



from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello, World!')
Do URL-binding in project urls.py file (minidjango_ver1/minidjango_ver1/urls.py)
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', views.home, name='home')
]
13. Run project with command python manage.py runserver 
14. Open browser http://127.0.0.1:8000/app1
15. when you install django 
16. you get django-admin CLI tool 
17. you get sqlite3 database 
18. you get development server