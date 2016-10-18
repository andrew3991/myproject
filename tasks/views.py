from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from .forms import TaskForm
from . import views
from tasks.models import Task
from projects.models import Project

import json

@login_required(login_url='/login/')
def tasks_table(req, project_id):
	try:
		project = Project.objects.get(pk=project_id)
	except Project.DoesNotExist:
		raise Http404("!!!!!")
	return render(req, 'tasks/index.html', {'project':project, 'form':TaskForm()})


@login_required(login_url='/login/')
def new_task(request, project_id):
	project = Project.objects.get(pk=project_id)
	if request.method == 'POST':
		if request.is_ajax():			
			task_name = request.POST.get('task_name')
			start_date = request.POST.get('start_date')
			end_date = request.POST.get('end_date')
			status = request.POST.get('status')
			response_data = {}

			task = Task(name=task_name, start_date=start_date, end_date=end_date, status=status, project=project)
			task.save()

			response_data['task_name'] = task.name
			response_data['start_date'] = task.start_date
			response_data['end_date'] = task.end_date
			response_data['status'] = task.status

			return JsonResponse(response_data)


def edit_task(request, project_id,  task_id):
	task = get_object_or_404(Task, pk=task_id)
	if request.method == "POST":
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			task = form.save(commit=False)
			task.save()
			return redirect('/tasks/task/%s/' % project_id)
	else:
		form=TaskForm(instance=task)
	return render(request, 'tasks/new_task.html',{'form':form})


def delete_task(request, project_id, task_id):
	task = get_object_or_404(Task, pk=task_id)
	task.delete()
	return redirect('/tasks/task/%s/' % project_id)

# def new_task(request, project_id):
# 	project = Project.objects.get(pk=project_id)
# 	if request.method == "POST":
# 		form = TaskForm(request.POST or None)
# 		if form.is_valid():
# 			task = form.save(commit=False)
# 			task.project = project
# 			task.save()
# 			url = reverse('tasks_table', args=[project_id])
# 			return HttpResponseRedirect(url)
# 	else:
# 		form = TaskForm()
# 	return render(request, 'tasks/tasks.html', {'project':project,'form':form})




