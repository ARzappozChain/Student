from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  
   path("AllCoursePage/", views.All_course_Page_views, name= 'All_Course_Page'),
   path('seminer_page/',views.Seminer_Page_views, name='seminer_page'),
   path('category/<slug:category_slug>/',views.Seminer_Page_views, name = 'seminer_page_category'),
    
]
