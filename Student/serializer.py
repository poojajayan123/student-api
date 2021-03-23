from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import exceptions
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class UserLoginSerializer(serializers.Serializer):   

    username  = serializers.CharField()
    password  = serializers.CharField()
    new_password = serializers.CharField(allow_null=True,allow_blank=True,required=False)
    def validate(self,data):
        username =  data.get("username")
        password =  data.get("password")
        new_password =  data.get("new_password","")
        if username and password:
            user = authenticate(username=username,password=password)
            if user is not None:
                user = User.objects.get(pk=user.pk)
                data['user'] = user
                if user.last_login==None:
                    if  new_password !="":
                        new_hashed_password = make_password(new_password)
                        user.password = new_hashed_password
                        user.save()
                    else:
                        msg= "New password required"
                        raise exceptions.ValidationError(msg)
                else:
                    msg="success"
            else:
                msg= "User not exist"
                raise exceptions.ValidationError(msg)
        else:
            msg = " username/ password required "
            raise exceptions.ValidationError(msg)
        return data