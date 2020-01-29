from django.shortcuts import render
from .models import Child
from django.http import HttpResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

def addChild(req):
	bool exists
	str message

	#Takes the request's POST data and makes it into a dictionary
	reqDic = req.POST
	#each attribute is accesed by the key in the request
	fname = req["name"]
	lname = req["lastname"]
	uname = req["username"]
	pword = req["password"]
	ag = req["age"]
	#this is a new child so their points will start off as zero
	pnts = 0

	checkChild = Child.objects.filter(first_name=fname, last_name=lname, username=uname, password=pword, age=ag, points=pnts)
	exists = False

	#checks to see if the child exists, if it doesnt an error will occur so that the 'exists' variable will stay False
	try:
		checkChild.first_name
	except:
		exists = True

	#A new child is created and saved.
	if exists == False:
		createdChild = Child(first_name=fname, last_name=lname, username=uname, password=pword, age=ag, points=pnts)
		createdChild.save()
		mesage = "True"

	#an appropriate message is returned if the child exists
	elif exists == True:
		message = "False: Child already exists"

	return message

	