from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^task/(?P<project_id>[0-9]+)/$', views.tasks_table, name='tasks_table'),
	url(r'^task/(?P<project_id>[0-9]+)/new/$', views.new_task, name='new_task'),
	url(r'^task/(?P<project_id>[0-9]+)/edit/(?P<task_id>[0-9]+)/$', views.edit_task, name='edit_task'),
	url(r'^task/(?P<project_id>[0-9]+)/delete/(?P<task_id>[0-9]+)/$', views.delete_task, name='delete_task'),
]