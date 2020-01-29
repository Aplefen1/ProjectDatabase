from django.shortcuts import render
from .models import Child
from django.http import HttpResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .methods import *

# Create your views here.
@csrf_exempt
def showChild(request):
	print("hello")
	if request.method == "POST":
		find = Child.objects.filter(username = request.POST['Username'])
		print(find)
		return HttpResponse(find)

@csrf_exempt
def newChild(request):
	print("new child called")
	if request.method == "POST":
		#the method will attempt to save the new child in the request, if it cant iot will return an error message, if it can it will return a success message
		response = addChild(request)
	else:
		response = "You have processed the wrong type of request"

	return HttpResponse(response)

		

@csrf_exempt
def confirmLogin(request):
	print("Login Resquest called")
	if request.method == "POST"
