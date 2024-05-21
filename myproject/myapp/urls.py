from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name='myaap'),
    path("about", views.about, name='about'),
    path("appointment", views.appointment, name='appointment'),
    path("blog", views.blog, name='blog'),
    path("contact", views.contact, name='contact'),
    path("bmi", views.bmi, name='bmi'),
    path("doctor", views.doctor, name='doctor'),
    path("gallery", views.gallery, name='gallery'),
    path("privacy", views.privacy, name='privacy'),
    path("terms", views.terms, name='terms'),
    path("signup",views.handelSignup, name='handelSignup'),
    path("login",views.handelLogin, name='handelLogin'),
    path("logout",views.handleLogout, name='handleLogout'),
    

]