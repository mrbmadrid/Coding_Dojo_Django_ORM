# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *

# Create your views here.

def index(request):
	return render(request, "courses/index.html", {'courses' : Course.objects.all()})

def add(request):
	if request.POST:
		Course.objects.create(name=request.POST['name'], desc=Description.objects.create(content=request.POST['desc']))
	return redirect(index)

def delete(request, id):
	if id == -1:
		return redirect(index)
	return render(request, "courses/delete.html", {'course' :Course.objects.get(id=id)})

def confirmdelete(request, id):
	Course.objects.get(id=id).delete()
	return redirect(index)
