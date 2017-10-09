from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.home, name = 'home'),
	url(r"^(?P<question_id>[0-9]+)", views.page, name = 'page'),
	url(r"^login/$",views.my_login, name = 'login'),
	url(r"^register/$", views.register, name = 'register'),
	url(r"^newquestion/$", views.new_question, name = 'new_question'),
	url(r"^profile/$", views.profile, name = 'profile'),
	url(r"^logout/$", views.my_logout, name = 'logout'),
	url(r"^upvote/(?P<question_id>[0-9]+)", views.upvote, name = 'upvote'),
	url(r"^downvote/(?P<question_id>[0-9]+)", views.downvote, name = 'downvote'),
	url(r"^remove_upvote/(?P<question_id>[0-9]+)", views.remove_upvote, name = 'remove_upvote'),
	url(r"^remove_downvote/(?P<question_id>[0-9]+)", views.remove_downvote, name = 'remove_downvote'),
]
