from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Question, Comment
import cloudinary

# Create your views here.
def home(request):
	#Get all the questions in database
	questions = Question.objects.all()
	today_datetime = timezone.now()
	if request.user.is_authenticated():
		upvotes = []
		downvotes = []
		for q in request.user.upvotes.all():
			upvotes.append(q.pk)
		for q in request.user.downvotes.all():
			downvotes.append(q.pk)
		return render(request, 'home.html', { 'time': today_datetime, 'questions': questions, 'user': request.user, 'upvotes': upvotes, 'downvotes': downvotes })
	return render(request, 'home.html', { 'time': today_datetime, 'questions': questions, 'user': request.user })

def page(request, question_id):
	if request.method == "POST":
		new_comment = Comment()
		new_comment.question = Question.objects.get(pk = question_id)
		new_comment.comment_text = request.POST['comment_text']
		new_comment.author = request.user
		new_comment.created_at = timezone.now()
		new_comment.save()
		return redirect('page', question_id=question_id)
	#Get the question with particular is
	question = Question.objects.get(pk = question_id)
	upvotes = []
	downvotes = []
	for u in question.upvotes.all():
		upvotes.append(u.username)
	for u in question.downvotes.all():
		downvotes.append(u.username)
	return render(request, 'page.html', { 'question': question, 'user': request.user, 'upvotes': upvotes, 'downvotes': downvotes })

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
		new_question.created_at = timezone.now()
		if request.FILES.get('picture', False):
			new_question.if_picture = True
		else:
			new_question.if_picture = False
		new_question.save()
		#Upload the picture to a different cloud server
		if new_question.if_picture:
			image_result = cloudinary.uploader.upload(
				request.FILES['picture'],
				public_id = "picture" + str(new_question.pk),
			)
		return redirect('home')
	else:
		return render(request, 'new_question.html', { 'user': request.user })

@login_required
def profile(request):
	if request.user.is_authenticated:
		questions = Question.objects.filter(author = request.user)
		return render(request, 'profile.html', {'user': request.user, 'questions': questions})
	else:
		return HttpResponse("You need to login to view this page!")

@login_required
def upvote(request, question_id):
	question = Question.objects.get(pk = question_id)
	user = request.user
	question.upvotes.add(user)
	return HttpResponse()

@login_required
def downvote(request, question_id):
	question = Question.objects.get(pk = question_id)
	user = request.user
	question.downvotes.add(user)
	return HttpResponse()

@login_required
def remove_upvote(request, question_id):
	question = Question.objects.get(pk = question_id)
	user = request.user
	question.upvotes.remove(user)
	return HttpResponse()

@login_required
def remove_downvote(request, question_id):
	question = Question.objects.get(pk = question_id)
	user = request.user
	question.downvotes.remove(user)
	return HttpResponse()
