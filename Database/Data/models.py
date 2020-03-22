from django.db import models
from .models import *

#This is the child model/ Table
class Child(models.Model):
    #Creating the fields
    #String field
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    #Integer Fields
    age = models.IntegerField()
    points = models.IntegerField(default=0)

    #Foriegn key fields
    #create many to one relationships with the other models
    classroom = models.ForeignKey('Classroom', default=None, on_delete=models.CASCADE, blank=True,null=True)
    teacher = models.ForeignKey('Teacher', default=None, on_delete=models.CASCADE, blank=True,null=True)
    school = models.ForeignKey('School', default=None, on_delete=models.CASCADE, blank=True,null=True)

    #creates a nice title for the child
    def __str__(self):
        title = self.first_name + ' ' + self.last_name
        return title

    #returns the info of the class
    def Info(self):
    	return self.first_name, self.last_name, self.username, self.password, self.age, self.points

#The teacher model
class Teacher(models.Model):
    #string fields
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    #Integer Fields
    age = models.IntegerField()

    #Many to one relatiopnships with the relevant models
    classroom = models.ForeignKey('Classroom', default=None, on_delete=models.CASCADE, blank=True,null=True)
    school = models.ForeignKey('School', default=None, on_delete=models.CASCADE, blank=True,null=True)

    #Title
    def __str__(self):
        title = self.first_name + ' ' + self.last_name
        return title

class Task(models.Model):
    #String Fields
    task_Name = models.CharField(max_length=32)
    task_Description = models.CharField(max_length=32)

    #Date Field Fields
    due_Date = models.DateField()

    teacher = models.ForeignKey('Teacher', default=None, on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        title = self.task_name
        return title

class Classroom(models.Model):
    #String Fields
    classroom_name = models.CharField(max_length=32)

    #Key Fields
    current_task = models.ForeignKey('Task', default=None, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        title = self.classroom_name
        return title

class School(models.Model):
    #String Fields
    name = models.CharField(max_length=32)

    def __str__(self):
        title = self.name
        return title