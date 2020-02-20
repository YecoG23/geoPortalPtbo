from django.forms import ModelForm
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField
from django.contrib.gis import forms

from .models import Localidad, Proyecto



class LocalidadForm(ModelForm):

	class Meta:
		model = Localidad
		exclude = '__all__'

class ProyectoForm(ModelForm):

	class Meta:
		model = Proyecto
		exclude = '__all__'
		widgets = {
			#'projeto': Select(choices = list(Projeto.objects.filter(profile__user__username=current_user.username).values_list('id','nome')) ) ,
			'ubicacion': forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}),
		}