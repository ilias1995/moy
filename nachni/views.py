from django.shortcuts import render
from models import Index, Glavnoe

def index(request):
	index = Index.objects.all()
	return render(request, 'nachni/index.html', {'index':index})
def register(request):
	return render(request, 'nachni/register.html')
def login(request):
	return render(request, 'nachni/login.html')
def glavnoe(request):
	return render(request, 'nachni/glavnoe.html')