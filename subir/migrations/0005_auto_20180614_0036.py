# Generated by Django 2.0.2 on 2018-06-14 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subir', '0004_auto_20180614_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='recetasadministracion',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='recetasadministracion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 6, 14, 0, 36, 0, 204066)),
        ),
    ]
