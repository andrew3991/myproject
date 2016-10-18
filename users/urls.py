from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^auth/register/$', views.register),
	url(r'^accounts/profile/$', views.profile ),
]