from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import ProjectForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from projects.models import Project
from django.contrib import auth
from django.template.context_processors import request


# class IndexView(generic.ListView):
# 	template_name = 'projects/home.html'
# 	context_object_name = 'projects'

# 	def get_queryset(self):
# 		return Project.objects.filter(start_date__lte=timezone.now()).order_by('-start_date')
@login_required(login_url='/login/')
def project_table(req, user_id):
	if req.user.is_active:
		userid = User.objects.get(pk=user_id)
		if req.user.id != userid.id:
			return redirect('/profile/')
		else:
			try:
				user = User.objects.get(pk=user_id)
				# user = auth.get_user(req).id
			except User.DoesNotExist:
				raise Http404("!!!!!")
			return render(req, 'projects/home.html', {'user':user, 'form':ProjectForm()})
	else:
		return redirect('/login/')


@login_required(login_url='/login/')
def project_new(request, user_id):
	user = User.objects.get(pk=user_id)
	if request.method == 'POST':
		if request.is_ajax():			
			project_name = request.POST.get('project_name')
			start_date = request.POST.get('start_date')
			end_date = request.POST.get('end_date')
			response_data = {}

			project = Project(name=project_name, start_date=start_date, end_date=end_date, user=user)
			project.save()

			response_data['project_name'] = project.name
			response_data['start_date'] = project.start_date
			response_data['end_date'] = project.end_date
			response_data['user_id'] = user.id

			return JsonResponse(response_data)


# def project_new(request):
# 	if request.method == "POST":
# 		form = ProjectForm(request.POST or None)
# 		if form.is_valid():
# 			project = form.save(commit=False)
# 			project.user = request.user
# 			project.save()
# 			return HttpResponseRedirect('/login/')
# 	else:
# 		form = ProjectForm()
# 	return render(request, 'projects/home.html', {'form':form})