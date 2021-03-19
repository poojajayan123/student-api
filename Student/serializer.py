from Student.models import StudentUser
from rest_framework import serializers

class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentUser
        fields = '__all__'