from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import Localidad, Proyecto
from .forms import LocalidadForm, ProyectoForm

# Create your views here.

#VIEW FOR INDEX
class HomeTemplateView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['proyectos'] = Proyecto.objects.all()
		return context

#LOCALIDAD

class LocalidadCreateView(CreateView):
	model = Localidad
	form_class = LocalidadForm
	success_url='/'

class ProyectoCreateView(CreateView):
	model = Proyecto
	form_class = ProyectoForm
	success_url='/'

	def form_valid(self, form):
		form.instance.show_map=True
		return super(ProyectoCreateView, self).form_valid(form)

class ProyectoUpdateView(UpdateView):
	model = Proyecto
	form_class = ProyectoForm
	success_url='/'

class ProyectoDeleteView(DeleteView):
	model = Proyecto
	success_url='/'
