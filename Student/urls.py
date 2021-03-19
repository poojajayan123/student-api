from django.contrib import admin
from django.urls import path
import Student as student
from Student import views
from django.conf.urls import url, include

urlpatterns = [
    path('login',views.student_login, name='student_login'),
    path('logout/',views.student_logout, name='student_logout'),
    path('change-password/<int:pk>',views.change_password, name='change_password'),

    path('register',views.create_student, name='create_student'),

    path('home/',views.student_home, name='student_home'),



]
