from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^projects/(?P<user_id>[0-9]+)/$', views.project_table, name='project_table'),
	url(r'^projects/(?P<user_id>[0-9]+)/new/$', views.project_new, name='project_new'),
]