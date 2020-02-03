from django.db import models
from .models import *

# Create your models here.
class Child(models.Model):
    child_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    age = models.IntegerField()
    points = models.IntegerField()

    Classroom_id = models.ForeignKey('Classroom', on_delete=models.CASCADE)
    Teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    School_id = models.ForeignKey('School', on_delete=models.CASCADE)

    def __str__(self):
        title = self.first_name + ' ' + self.last_name
        return title

    def Info(self):
    	return self.first_name, self.last_name, self.username, self.password, self.age, self.points

    def Id(self):
        return self.child_id

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()

    def __str__(self):
        title = self.first_name + ' ' + self.last_name
        return title

    def Id(self):
        return self.teacher_id

class Task(models.Model):
    task_name = models.CharField(max_length=32)
    task_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=32)

    def Id(self):
        return self.task_id

    def __str__(self):
        title = self.task_name
        return title

class Classroom(models.Model):
    Classroom_id = models.AutoField(primary_key=True)
    classroom_name = models.CharField(max_length=32)

    def __str__(self):
        title = self.classroom_name
        return title

class School(models.Model):
    School_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        title = self.name
        return title