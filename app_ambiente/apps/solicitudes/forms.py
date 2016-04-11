# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class SolicitudForm(forms.ModelForm):
	class Meta:
		model = SolicitudUser
		fields = '__all__'
		exclude = ('user',)

	def __init__(self, *args, **kwargs):
		super(SolicitudForm, self).__init__(*args, **kwargs)
		self.fields['peso_aprox'].widget = widgets.TextInput(attrs = {'class': 'form-control'})
		self.fields['material'].widget = widgets.Select(choices = Material.objects.all().values_list('pk', 'nombre'), attrs = {'class': 'form-control'})