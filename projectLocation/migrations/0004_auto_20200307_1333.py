# Generated by Django 2.2.9 on 2020-03-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectLocation', '0003_proyecto_show_map'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='show_map',
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_creacion',
            field=models.DateTimeField(blank=True),
        ),
    ]