from django.shortcuts import render
import datetime
from .models import Question

# Create your views here.
def home(request):
	questions = Question.objects.all()
	today_datetime = datetime.datetime.now()
	return render(request, 'home.html', { 'time': today_datetime, 'questions': questions })

def page(request, id):
	return render(request, 'page.html', { 'id': id })

def login(request):
	return render(request, 'login.html', {})

def register(request):
	return render(request, 'register.html', {})

def profile(request):
	return render(request, 'profile.html', {})
