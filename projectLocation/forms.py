from django.forms import ModelForm, CheckboxInput
from django.forms.models import ModelChoiceField, ModelMultipleChoiceField
from django.contrib.gis import forms

from leaflet.forms.widgets import LeafletWidget
from leaflet.forms.fields import PointField

from .models import Localidad, Proyecto



class LocalidadForm(ModelForm):

	class Meta:
		model = Localidad
		exclude = '__all__'


LEAFLET_WIDGET_ATTRS = {
    'map_height': '600px',
    'default_lat':'-10.774303',
    'default_lon':'-75.813227',
    'default_zoom':'10',
    # 'map_width': '100%',
    # 'display_raw': 'true',
    # 'map_srid': 4326,
}

class ProyectoForm(ModelForm):
	# geom = PointField()

	class Meta:
		model = Proyecto
		exclude = '__all__'
		widgets = {
			# 'geom': forms.OSMWidget(attrs=LEAFLET_WIDGET_ATTRS),
			'geom':LeafletWidget(),
			# 'show_map':CheckboxInput(default=True)
		}