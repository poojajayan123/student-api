from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import user_logged_in, authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.



# def login(rself,equest):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user:
#         login(request,user)
#         msg="Logged in"
#         return HttpResponseRedirect('/home')
#     else:
#         return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def home(request):
    if request.method=="GET":
        
        return render(request,"users/home.html")

def user_logout(request):
    logout(request)
    messages.info(request,"Logged out")
    return redirect("users:login")

def user_login(request):
    if request.method == "POST":
        form =  AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            if user is not None:
                # login(request)
                messages.info(request,f"You are now logged in as{username}")
                return redirect(reverse("users:home"))
            else:
                messages.error(request,"Invalid user")
        else:
                messages.error(request,"Invalid user")
    form = AuthenticationForm()
    return render(request,"users/login.html",{"form":form})
