from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import Localidad, Proyecto
from .forms import LocalidadForm, ProyectoForm

# Create your views here.


#CUSTOM FUNCTION TO RENDER CHARJS
#MODALIDAD DE EJECUCION DE LOS PROYECTOS

# TIPOS_EJECUCION = [
#     ("OPC", "Por Contrata"),
#     ("OAD", "Por Administracion Directa"),
# ]
data1_mod_ejec = Proyecto.objects.filter(modalidad_ejecucion="OPC").count()
data2_mod_ejec = Proyecto.objects.filter(modalidad_ejecucion="OAD").count()
arr_data_mod_ejec = [data1_mod_ejec, data2_mod_ejec]
label1_mod_ejec = "Por Contrata - {}".format(data1_mod_ejec)
label2_mod_ejec = "Por Administracion Directa - {}".format(data2_mod_ejec)
arr_label_mod_ejec = [label1_mod_ejec, label2_mod_ejec]

#TIPO DE SECTORES DE LOS PROYECTOS
# TIPOS_SECTORES = [
#     ("AG", "Agricultura"),
#     ("ED","Educacion"),
#     ("EG","Energia"),
#     ("SA","Salud"),
#     ("TC","Transporte y Comunicaciones"),
#     ("VCS","Vivienda, Construccion y Saneamiento"),
#     ("O","Otros"),
# ]
data1_tip_sec = Proyecto.objects.filter(sector_financiamiento="AG").count()
data2_tip_sec = Proyecto.objects.filter(sector_financiamiento="ED").count()
data3_tip_sec = Proyecto.objects.filter(sector_financiamiento="EG").count()
data4_tip_sec = Proyecto.objects.filter(sector_financiamiento="SA").count()
data5_tip_sec = Proyecto.objects.filter(sector_financiamiento="TC").count()
data6_tip_sec = Proyecto.objects.filter(sector_financiamiento="VCS").count()
data7_tip_sec = Proyecto.objects.filter(sector_financiamiento="O").count()

arr_data_tip_sec = [
		data1_tip_sec, 
		data2_tip_sec,
		data3_tip_sec,
		data4_tip_sec,
		data5_tip_sec,
		data6_tip_sec,
		data7_tip_sec
	   ]

label1_tip_sec = "Agricultura - {}".format(data1_tip_sec)
label2_tip_sec = "Educacion - {}".format(data2_tip_sec)
label3_tip_sec = "Energia - {}".format(data3_tip_sec)
label4_tip_sec = "Salud - {}".format(data4_tip_sec)
label5_tip_sec = "Transporte y Comunicaciones - {}".format(data5_tip_sec)
label6_tip_sec = "Vivienda, Construccion y Saneamiento - {}".format(data6_tip_sec)
label7_tip_sec = "Otros - {}".format(data7_tip_sec)

arr_label_tip_sec = [
		label1_tip_sec, 
		label2_tip_sec,
		label3_tip_sec,
		label4_tip_sec,
		label5_tip_sec,
		label6_tip_sec,
		label7_tip_sec
	   ]

# TIPOS_ESTADOS_OBRAS = [
#     ("F","Finalizada"),
#     ("E","En ejecucion"),
#     ("P","Paralizada"),
#     ("SE","Sin ejecucion"),
# ]
data1_tip_est = Proyecto.objects.filter(estado_obra="F").count()
data2_tip_est = Proyecto.objects.filter(estado_obra="E").count()
data3_tip_est = Proyecto.objects.filter(estado_obra="P").count()
data4_tip_est = Proyecto.objects.filter(estado_obra="SE").count()

arr_data_tip_est = [
		data1_tip_est, 
		data2_tip_est,
		data3_tip_est,
		data4_tip_est,
	   ]

label1_tip_est = "Finalizada - {}".format(data1_tip_est)
label2_tip_sec = "En ejecucion - {}".format(data2_tip_est)
label3_tip_sec = "Paralizada - {}".format(data3_tip_est)
label4_tip_sec = "Sin ejecucion - {}".format(data4_tip_est)

arr_label_tip_est = [
		label1_tip_est, 
		label2_tip_sec,
		label3_tip_sec,
		label4_tip_sec,
	   ]


#VIEW FOR INDEX
class HomeTemplateView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['proyectos'] = Proyecto.objects.all()
		context['arr_data_mod_ejec'] = arr_data_mod_ejec
		context['arr_label_mod_ejec'] = arr_label_mod_ejec
		context['arr_data_tip_sec'] = arr_data_tip_sec
		context['arr_label_tip_sec'] = arr_label_tip_sec
		context['arr_data_tip_est'] = arr_data_tip_est
		context['arr_label_tip_est'] = arr_label_tip_est
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
