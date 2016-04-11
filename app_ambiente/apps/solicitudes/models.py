from django.db import models
from django.contrib.auth.models import User

class Material(models.Model):
	nombre = models.CharField(max_length = 20)
	precio = models.DecimalField(max_digits = 11, decimal_places = 2)
	peso = models.DecimalField(max_digits = 5, decimal_places = 2)

class Bodega(models.Model):
	nombre = models.CharField(max_length = 30)
	direccion = models.CharField(max_length = 40)

	def __str__(self):
		return self.nombre

class BodegaMaterial(models.Model):
	material = models.ForeignKey(Material)
	bodega = models.ForeignKey(Bodega)

class SolicitudUser(models.Model):
	user = models.ForeignKey(User)
	bodega_material = models.ForeignKey(BodegaMaterial)
	peso_aprox = models.DecimalField(max_digits = 11, decimal_places = 2)