from django.views.static import serve
from django.contrib import admin
from django.conf.urls import  url, include
from django.urls import path
from django.conf import settings
from users import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    #path('login/', admin.site.urls),
    path('api/student/',include('Student.urls')),
    path('polls/',include('polls.urls')),

    url(r'^admin/', admin.site.urls),
    path('', include(('users.urls','users'),namespace="users")),    


    url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_FILE_ROOT}),
]
