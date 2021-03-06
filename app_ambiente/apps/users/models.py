from django.contrib.auth.models import User
from django.db import models

class TypeProfile(models.Model):
	nombre = models.CharField(max_length = 30)

	def __str__(self):
		return self.nombre

class ProfileUser(models.Model):
	user = models.OneToOneField(User, primary_key = True)
	foto = models.ImageField(upload_to = 'img/users/', default = 'img/users/none.png', blank = True)
	numero_celular = models.CharField(max_length = 10, blank = True, null = True)
	direccion = models.CharField(max_length = 40, blank = True, null = True)
	type_profile = models.ForeignKey(TypeProfile)
	key_user = models.CharField(max_length = 60, blank = True, null = True)

	def __str__(self):
		return str(self.user)