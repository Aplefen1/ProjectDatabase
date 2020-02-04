from django.db import models
from .models import *

# Create your models here.
#This is the child model
class Child(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    age = models.IntegerField()
    points = models.IntegerField(default=0)

    #create many to one rerlationships with the other models
    classroom = models.ForeignKey('Classroom', default=None, on_delete=models.CASCADE, blank=True,null=True)
    teacher = models.ForeignKey('Teacher', default=None, on_delete=models.CASCADE, blank=True,null=True)
    school = models.ForeignKey('School', default=None, on_delete=models.CASCADE, blank=True,null=True)

    #creates a nice title for the child
    def __str__(self):
        title = self.first_name + ' ' + self.last_name
        return title

    def Info(self):
    	return self.first_name, self.last_name, self.username, self.password, self.age, self.points

#The teacher model
class Teacher(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField()

    #Many to one relatiopnships with the relevant models
    classroom = models.ForeignKey('Classroom', default=None, on_delete=models.CASCADE, blank=True,null=True)
    school = models.ForeignKey('School', default=None, on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        title = self.first_name + ' ' + self.last_name
        return title

class Task(models.Model):
    task_name = models.CharField(max_length=32)
    task = models.CharField(max_length=32)

    teacher = models.ForeignKey('Teacher', default=None, on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        title = self.task_name
        return title

class Classroom(models.Model):
    classroom_name = models.CharField(max_length=32)

    current_task = models.ForeignKey('Task', default=None, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        title = self.classroom_name
        return title

class School(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        title = self.name
        return title