
from django.contrib import admin
from django.conf.urls import  url, include
from django.urls import path
from users import views


urlpatterns = [
    path('',views.home,name='home'),
    path('logout/', views.user_logout,name="logout"),
    path('login/',views.user_login,name="login"),

    # path('home',views.home,name='home')
]
