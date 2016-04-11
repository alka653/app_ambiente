from .forms import *
from .models import *
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required

class SolicitudView(CreateView):
	model = SolicitudUser
	form_class = SolicitudForm
	template_name = 'solicitud/make_solicitud.html'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(SolicitudView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(SolicitudView, self).get_context_data(**kwargs)
		context['title'] = 'Solicitar'
		return context