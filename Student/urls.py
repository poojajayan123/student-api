from django.contrib import admin
from django.urls import path
from Student.views import UserLoginView
from django.conf.urls import url, include
from Student import views

urlpatterns = [
    path('login',UserLoginView.as_view(),name="login"),
    # path('logout/',UserLogOutView.as_view()),
    # path('change-password/<int:pk>',views.change_password, name='change_password'),

    path('register',views.create_student, name='create_student'),

    # path('home/',views.student_home, name='student_home'),



]
