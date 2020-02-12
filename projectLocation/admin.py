from django.contrib import admin
from .models import Localidad, Proyecto

# Register your models here.
admin.site.register(Localidad, admin.ModelAdmin)
admin.site.register(Proyecto, admin.ModelAdmin)