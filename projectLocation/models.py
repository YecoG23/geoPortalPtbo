from django.db import models
from django.contrib.gis import models as gismodels
# Create your models here.


class Localidad (models.Model):
	nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Proyecto (gismodels.Model):
	nombre = models.CharField(max_length=100)
	ubicacion = gismodels.PointField()
	

    def __str__(self):
        return self.nombre