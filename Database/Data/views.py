from django.shortcuts import render
from .models import Child
from django.http import HttpResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

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
		reqDic = request.POST
		fname = reqDic["name"]
		lname = reqDic["lastname"]
		uname = reqDic["username"]
		pword = reqDic["password"]
		ag = reqDic["age"]
		pnts = 0

		createdChild = Child(first_name=fname, last_name=lname, username=uname, password=pword, age=ag, points=pnts)
		createdChild.save()

