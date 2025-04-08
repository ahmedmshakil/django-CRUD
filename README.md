# django-CRUD

<!-- setup > -->
- go to django-CRUD folder
- cd django-crud
 <!--create virtual env  -->
 - python3 -m venv crudenv
 - source crudenv/bin/activate (Ubuntu 24.4)
 - pip install django
 <!-- check env working or not -->
 - pip freeze

 <!-- how to run  -->
 - cd crud
 - python3 manage.py runserver

 <!-- added new app folder -->
 - cd crud
 - django-admin startapp myapp

``file instruction``
 - crud is the root folder
 - myapp is the application folder


# root directory (CRUD )
# django 5.2
# crud
 ├── crud  
 │   ├── __init__.py
 │   ├── settings.py
 │   ├── urls.py
 │   └── wsgi.py
 ├── myapp
 │   ├── __init__.py
 │   ├── admin.py
 │   ├── apps.py
 │   ├── migrations
 │   │   └── __init__.py
 │   ├── models.py
 │   ├── tests.py
 │   └── views.py
 ├── manage.py
 └── templates
    └── index.html


- python3 manage.py shell, it will go to interactive console of the database
- from myapp.models import Student
` it will print the database `
- Student.objects.all()

` fetch specific record `
- s1 = Student.objects.get(name = "shakil")