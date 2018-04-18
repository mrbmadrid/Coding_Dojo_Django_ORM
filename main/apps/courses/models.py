# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Description(models.Model):
	content = models.TextField(default="None")

class Course(models.Model):
	name = models.CharField(max_length=255)
	desc = models.OneToOneField(Description, related_name="course")
	created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	content = models.TextField(default="None")
	course = models.ForeignKey(Course, related_name="comments")
