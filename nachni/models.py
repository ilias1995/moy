from django.db import models
from django import forms

class Index(models.Model):
	title = models.CharField(max_length=100)
	head = models.CharField(max_length=100)
	nazvanie = models.CharField(max_length=200)
	context = models.TextField()

class Glavnoe(models.Model):
	title = models.CharField(max_length=100)
	head = models.CharField(max_length=100)
	nazvanie = models.CharField(max_length=200)
	text_info = models.TextField()

class Register(models.Model):
	name = models.CharField(max_length=200)
	f_name = models.CharField(max_length=200)
	email = models.EmailField()
	password = models.CharField(max_length=200) 

