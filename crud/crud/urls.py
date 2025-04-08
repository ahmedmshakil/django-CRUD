"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('info/', views.info),
    path('',include('myapp.urls')),
]


# root directory (CRUD )
# django 5.2
# crud
# ├── crud  
# │   ├── __init__.py
# │   ├── settings.py
# │   ├── urls.py
# │   └── wsgi.py
# ├── myapp
# │   ├── __init__.py
# │   ├── admin.py
# │   ├── apps.py
# │   ├── migrations
# │   │   └── __init__.py
# │   ├── models.py
# │   ├── tests.py
# │   └── views.py
# ├── manage.py
# └── templates
#     └── index.html




            