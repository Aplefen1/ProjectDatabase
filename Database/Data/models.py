from django.db import models

# Create your models here.
class Child(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    age = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        title = self.first_name + ' ' + self.last_name
        return title

    def Info(self):
    	return self.first_name, self.last_name, self.username, self.password, self.age, self.points

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        title = self.first_name + ' ' + self.last_name
        return title

class Task(models.Model):
