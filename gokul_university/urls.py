from django.urls import path
from gokul_university import views
urlpatterns = [
    path('', views.func),

     path('about', views.about, name="myabout"), 
    path('course', views.course, name="mycourse"), 
    path('admission', views.admission, name="myadmission"), 
    path('news', views.news, name="mynews"), 
    path('contact', views.contact, name="mycontact"), 
   

]