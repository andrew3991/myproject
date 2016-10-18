from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views as auth_views
from users.forms import LoginForm


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^', include('users.urls')),
	url(r'^login/$', auth_views.login, {'template_name': 'users/login.html', 'authentication_form': LoginForm}, name='login'),
	url(r'^', include('projects.urls')),
	url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
    
]
