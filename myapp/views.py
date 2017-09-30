from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
	today_datetime = datetime.datetime.now()
	return render(request, 'home.html', { 'time': today_datetime })

def page(request, id):
	return render(request, 'page.html', { 'id': id })
