"""
URL configuration for university_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from gokul_university import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('punjab', include('punjab_university.urls')), 
    path('', include('gokul_university.urls')), 
    path('chandigarh', include('chandigarh_university.urls')), 
    path('about', views.about), 
    path('course', views.course), 
    path('admission', views.admission), 
    path('news', views.news), 
    path('contact', views.contact), 
]