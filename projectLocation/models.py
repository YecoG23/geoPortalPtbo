from django.db import models
from django.contrib.gis.db import models as gismodels
from django.urls import reverse
from datetime import datetime
# Create your models here.


class Localidad (models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Localidades"

TIPOS_EJECUCION = [
    ("Por Contrata", "OPC"),
    ("Por Administracion Directa", "OAD"),
]

TIPOS_SECTORES = [
    ("Agricultura", "AG"),
    ("Educacion", "ED"),
    ("Energia", "EG"),
    ("Salud", "SA"),
    ("Transporte y Comunicaciones", "TC"),
    ("Vivienda, Construccion y Saneamiento", "VCS"),
    ("Otros", "O"),
]

TIPOS_ESTADOS_OBRAS = [
    ("Finalizada", "F"),
    ("En ejecucion", "E"),
    ("Paralizada", "P"),
    ("Sin ejecucion", "SE"),
]

class Proyecto (gismodels.Model):
	entidad = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)
	modalidad_ejecucion = models.CharField(max_length=100, choices=TIPOS_EJECUCION)
	# fecha_inicio = models.DateTimeField(blank=True, default=datetime.now())
	contratista = models.CharField(max_length=100)
	supervisor = models.CharField(max_length=100)
	residente = models.CharField(max_length=100)
	sector_financiamiento = models.CharField(max_length=100, choices=TIPOS_SECTORES)
	estado_obra = models.CharField(max_length=100, choices=TIPOS_ESTADOS_OBRAS)
	geom = gismodels.PointField()
	localidad = models.ForeignKey(Localidad,on_delete=models.CASCADE)
	fecha_creacion = models.DateField(blank=True)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('update_proyecto', kwargs={'pk': self.pk})

	@property
	def popupContent(self):
		return '<strong>{}</strong><hr><p class="text-muted"><strong>Localidad:</strong>{}</br><strong>Coordinadas:</strong> {},{}</p>'.format(self.nombre,self.localidad,self.geom.x,self.geom.y)
	