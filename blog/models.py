from django.db import models
from django import forms

class BlogPost(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	timestamp = models.DateTimeField()


class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	e-mail = forms.EmailField(required=False)
	message = forms.TextField()
