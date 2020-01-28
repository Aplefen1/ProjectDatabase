from django.shortcuts import render
from .models import insertChild
from django.http import HttpResponse

# Create your views here.
def insertChild(request):
	if request.method = "POST":
		print(request.POST)