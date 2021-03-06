from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, logout, login
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import redirect, render
from Student.password import password_generator
from rest_framework import serializers
from Student.serializer import StudentUserSerializer, UserLoginSerializer

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser , MultiPartParser, FormParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import TemplateHTMLRenderer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authtoken.models import Token

from django.contrib.auth.hashers import make_password, check_password





class UserLoginView(APIView):

    def post(self,request):
        
        login_serializer  = UserLoginSerializer(data= request.data)
        login_serializer.is_valid(raise_exception=True)
        user =  login_serializer.validated_data['user']            
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)        
        return Response({"token": token.key,'user_id': user.pk,
            'email': user.email}, status=200)


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

@csrf_exempt
@api_view(['POST'])
def  create_student(request):
    if request.method == 'POST':
        #student_data = JSONParser().parse(request.data)
        
        password  = password_generator(6)
        hash_password=make_password(password)
        student_serializer = StudentUserSerializer(data=request.data)
        # print(student_serializer.is_valid())
        # student_serializer.password = hash_password
        if student_serializer.is_valid():
            student_serializer.save(password=hash_password)
            return Response({'Temporary-password': password})
        else:
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

