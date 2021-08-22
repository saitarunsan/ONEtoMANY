from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
