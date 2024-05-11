from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
  
  path('Register/', views.Register, name='Registerpage'),
  path('Login/', views.LoginView, name='loginpage'),
  path('Logout/', views.LogoutView, name='logoutpage'),
]
