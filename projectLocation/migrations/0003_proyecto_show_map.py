# Generated by Django 2.2.9 on 2020-03-04 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectLocation', '0002_auto_20200221_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='show_map',
            field=models.BooleanField(default=True),
        ),
    ]
