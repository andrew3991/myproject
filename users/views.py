from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf

# def login(request):
# 	args = {}
# 	args.update(csrf(request))
# 	if request.POST:
# 		username = request.POST.get('username', '')
# 		password = request.POST.get('password', '')
# 		user = auth.authenticate(username=username, password=password)
# 		if user is not None:
# 			auth.login(request, user)
# 			return redirect('projects/')
# 		else:
# 			args['login_error'] = "User find not!!!"
# 			return render_to_response('users/login.html', args)
# 	else:
# 		render_to_response('users/login.html', args)

# def logout(request):
# 	auth.logout(request)
# 	return redirect("/")


@login_required
def profile(request):
    url = '/projects/%s/' % request.user.id
    return HttpResponseRedirect(url)
   
   
def register(request):
	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()
	if request.POST:
		newuser_form = UserCreationForm(request.POST)
		if newuser_form.is_valid():
			newuser_form.save()
			newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
			 password=newuser_form.cleaned_data['password2'])
			auth.login(request, newuser)
			return redirect('/')
		else:
			args['form'] = newuser_form
	return render_to_response('users/registration.html', args)


