from djongo import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        abstract = True
        db_table = "student"

    def __unicode__(self):
        return self.name