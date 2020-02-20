from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Localidad, Proyecto
from .forms import LocalidadForm, ProyectoForm

# Create your views here.

#VIEW FOR INDEX


#LOCALIDAD

class LocalidadCreateView(CreateView):
	model = Localidad
	form_class = LocalidadForm
	success_url='/'

class ProyectoCreateView(CreateView):
	model = Proyecto
	form_class = ProyectoForm
	success_url='/'