from django.shortcuts import render
from .models import Child
from .models import Classroom
from django.http import HttpResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
import json

def addChild(req):

	#Takes the request's POST data and makes it into a dictionary
	reqDic = req.POST
	#each attribute is accesed by the key in the request
	fname = reqDic["name"]
	lname = reqDic["lastname"]
	uname = reqDic["username"]
	pword = reqDic["password"]
	ag = reqDic["age"]
	#this is a new child so their points will start off as zero
	pnts = 0

	#finds a query set of all the objects that are duplicates
	checkChild = Child.objects.filter(username=uname)

	#checks to see if the child exists, if it doesnt an error will occur so that the 'exists' variable will stay False
	#if finding the username gives an error
	try:
		checkChild[0].username
	#then the child doesnt exist
	except:
		exists = False
	#otherwise it does exist
	else:
		print("This user does exist", checkChild)
		exists = True

	#an appropriate message is returned if the child exists
	if exists == True:
		message = "False: Child already exists"

	else:
		#A new child is created and saved.
		createdChild = Child(first_name=fname, last_name=lname, username=uname, password=pword, age=ag, points=pnts)
		createdChild.save()
		message = "True"


	return message

def checkLogin(req):

	reqDic = req.POST
	username = reqDic["username"]
	password = reqDic["password"]

	subject = Child.objects.filter(username=username)

	if subject[0].password == password:
		return "True"
	
	else:
		return "False"

def getStudentsFromClass(req):
	reqDic = req.POST
	classname = reqDic["classname"]

	#First find the classroom with the given name
	findClass = Classroom.objects.filter(classroom_name=classname)
	#Then take the id of that classroom
	classroomId = findClass[0].id
	#Then find all the students withg that id in their classroom field
	students = Child.objects.filter(classroom=classroomId)

	responseDict = {}
	li = []
	for stud in students:
		stu = {}
		stu["name"] = stud.first_name+stud.last_name
		stu["points"] = stud.points
		li.append(stu)

	print(li)
	responseDict["children"] = li
	return responseDict

def returnClassrooms(req):
	classrooms = Classroom.objects.all()
	responseDict = {}
	responseList = []

	for cl in classrooms:
		responseList.append(cl.classroom_name)

	responseDict['names'] = responseList
	responseDict['length'] = len(responseList)
	
	return responseDict

def GetChildData(req):
	reqDic = req.POST
	uname = reqDic["username"]

	findChild = Child.objects.filter(username=uname)
	child = findChild[0]
	print(child)

	responseDict = {}

	responseDict["firstname"] = child.first_name
	responseDict["lastname"] = child.last_name
	responseDict["username"] = child.username
	responseDict["age"] = child.age
	responseDict["points"] = child.points

	return responseDict
