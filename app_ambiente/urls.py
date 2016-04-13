from django.conf.urls import include, url
from django.contrib import admin

# Django Rest Api
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email')

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include(router.urls)),
	url(r'^rest-auth/', include('rest_auth.urls')),
	url(r'^rest-auth/registrate/', include('rest_auth.registration.urls')),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^', include('app_ambiente.apps.principal.urls')),
	url(r'^users/', include('app_ambiente.apps.users.urls')),
	#url(r'^accounts/', include('allauth.urls')),
	url(r'^solicitudes/', include('app_ambiente.apps.solicitudes.urls')),
]
