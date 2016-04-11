from django.views.generic import TemplateView
from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('app_ambiente.apps.soap_server.views',
	url(r'^auth-user/$', 'auth_user', name = 'auth_user'),
)