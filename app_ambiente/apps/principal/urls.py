from django.views.generic import TemplateView
from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('app_ambiente.apps.principal.views',
	url(r'^$', TemplateView.as_view(template_name = 'home/index.html'), {'title': 'Bienvenido'}, name = 'home'),
)