from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, logout, login
from rest_framework.decorators import api_view
from django.contrib import messages
from Student.models import StudentUser
from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import redirect, render
from Student.password import password_generator
from rest_framework import serializers
from Student.serializer import StudentUserSerializer

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser , MultiPartParser, FormParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import TemplateHTMLRenderer



def student_login(request):
    # if request.method == 'POST'
    #     form = AuthenticationForm(request,data=request.POST)
    #     user = authenticate(username=Username,password=password)
    #     login(request,data)
    #     message = "success"
    #     return JsonResponse(request,message)
    # else
    #     form = AuthenticationForm()

    pass
        

def student_logout(request):
    pass

def student_home(request):
    pass

@csrf_exempt
@api_view(['POST'])
def  create_student(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request,data)
    #     if form.is_valid():
    #         password_length = 6
    #         password = password_generator(password_length)
    #         form.temp_password = password
    #         form.is_superuser = False
    #         form.save()
    #         messages = "user created"
    #         return redirect(reverse("Student:student_home"))
    #     else:
    #         message = "invalid"
    # else:
    #     form = UserCreationForm()
    #     return redirect(reverse("student:create_student"),{ "form" : form})

    if request.method == 'POST':
        #student_data = JSONParser().parse(request.data)
        student_serializer = StudentUserSerializer(data=request.data)
        if student_serializer.is_valid():
            password =password_generator(6)
            print(password)
            student_serializer.save(temp_password=password)
            # content = {"password": password}
            # return Response(content=password, status=status.HTTP_201_CREATED) 
            # return Response(json.dumps(content), content_type='application/json')
            return Response({'Temporary-password': password})
        else:
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)