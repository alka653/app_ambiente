from app_ambiente.apps.soap_server.api import *
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from .api import LoginResource
from tastypie.api import Api

ambiente_api = Api(api_name = 'ambiente')
ambiente_api.register(LoginResource())

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include(ambiente_api.urls)),
	url(r'^', include('app_ambiente.apps.principal.urls')),
	url(r'^users/', include('app_ambiente.apps.users.urls')),
	url(r'^solicitudes/', include('app_ambiente.apps.solicitudes.urls')),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
