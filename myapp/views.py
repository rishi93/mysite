from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Question

# Create your views here.
def home(request):
	questions = Question.objects.all()
	today_datetime = timezone.now()
	return render(request, 'home.html', { 'time': today_datetime, 'questions': questions, 'user': request.user })

def page(request, id):
	return render(request, 'page.html', { 'id': id })

def my_login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('profile')
		else:
			return HttpResponse("Wrong login credentials")
	else:
		return render(request, 'login.html', {})

def my_logout(request):
	logout(request)
	return redirect('home')

def register(request):
	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password1']
		user = User.objects.create_user(username, email, password)
		user.save()
		return HttpResponse("Your data has been saved!")
	else:
		return render(request, 'register.html', {})

@login_required
def new_question(request):
	if request.method == "POST":
		new_question = Question()
		new_question.question_text = request.POST['question_text']
		new_question.author = request.user
		new_question.save()
		return HttpResponse("Your question was submitted successfully!")
	else:
		return render(request, 'new_question.html', { 'user': request.user })

@login_required
def profile(request):
	if request.user.is_authenticated:
		return render(request, 'profile.html', {'user': request.user})
	else:
		return HttpResponse("You need to login to view this page!")
