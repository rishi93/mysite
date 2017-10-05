from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.home, name = 'home'),
	url(r"^(?P<id>[0-9]+)", views.page, name = 'page'),
	url(r"^login/$",views.my_login, name = 'login'),
	url(r"^register/$", views.register, name = 'register'),
	url(r"^profile/$", views.profile, name = 'profile'),
	url(r"^logout/$", views.my_logout, name = 'logout')
]
