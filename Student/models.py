from djongo import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class StudentUser(AbstractUser):
    temp_password = models.CharField(max_length=10)

    class Meta:
        db_table = 'StudentUser'
       
    def __str__(self):
        return self.temp_password


class student(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        abstract = True
        db_table = "student"

    def __unicode__(self):
        return self.name