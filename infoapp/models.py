from django.db import models

# Create your models here.
#creating student models
class Student(models.Model):
    #attributes of Student
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phnumber = models.IntegerField()
    address = models.CharField(max_length=200)
