from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('course_detail_page/<int:id>/',views.CourseDetailsPage, name='CourseDetailsPage'),
   
   
]
