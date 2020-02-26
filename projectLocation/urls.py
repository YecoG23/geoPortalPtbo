from django.urls import path

from .views import LocalidadCreateView, ProyectoCreateView


urlpatterns = [
	path('localidad/add',LocalidadCreateView.as_view(), name='add_localidad'),
	path('add',ProyectoCreateView.as_view(), name='add_proyecto'),


]