from django.urls import path

from .views import LocalidadCreateView, ProyectoCreateView, ProyectoUpdateView, ProyectoDeleteView



urlpatterns = [
# LOCALIDADES
	path('localidad/add',LocalidadCreateView.as_view(), name='add_localidad'),
# PROYECTOS
	path('add',ProyectoCreateView.as_view(), name='add_proyecto'),
	path('<int:pk>/update',ProyectoUpdateView.as_view(), name='update_proyecto'),
	path('<int:pk>/delete',ProyectoDeleteView.as_view(), name='delete_proyecto'),
]