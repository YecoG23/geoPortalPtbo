# Generated by Django 2.2.9 on 2020-02-21 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectLocation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='localidad',
            options={'verbose_name_plural': 'Localidades'},
        ),
        migrations.RenameField(
            model_name='proyecto',
            old_name='ubicacion',
            new_name='geom',
        ),
    ]
