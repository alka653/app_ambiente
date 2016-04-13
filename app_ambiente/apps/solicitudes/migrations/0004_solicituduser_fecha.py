# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0003_remove_bodegamaterial_peso'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicituduser',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
