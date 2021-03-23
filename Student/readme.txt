from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, logout, login
from rest_framework.decorators import api_view
from django.contrib import messages
from django.contrib.auth.models import User
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
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
@api_view(['POST'])
def student_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        
        stud_user = User.objects.filter(username=username, temp_password=password).first()
        # stud_user = authenticate(username=username, temp_password=password)
        print(stud_user)
        message =""
        if stud_user is not None:             
            login(request,stud_user)
            message = "Login sucess"
            # return redirect(reverse('Student:change_password'))
        else:
            message = "Login Failed"
        return Response({"message" : message})
        # return JsonResponse(tutorials_serializer.data, safe=False)
    

def student_logout(request):
    pass

def student_home(request):
    pass

@csrf_exempt
@api_view(['POST'])
def  create_student(request):

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

@csrf_exempt
@api_view(['PUT'])
def change_password(request,pk): 
    if request.method == 'PUT':
        # user_data = JSONParser().parse(request)
        student = User.objects.filter(pk=pk).first()
        # old_password = request.data.get('old_password')
        # new_password = request.data.get('new_password')
        # user_serializer = StudentUserSerializer(data = request.data)
        # if user_serializer.is_valid():
        #     user_serializer.save()

         
        user_serializer = StudentUserSerializer(student, data=request.data) 
        if user_serializer.is_valid(): 
            user_serializer.save() 
            return Response(user_serializer.data) 
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 