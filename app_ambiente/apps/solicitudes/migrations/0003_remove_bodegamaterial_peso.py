# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0002_auto_20160412_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bodegamaterial',
            name='peso',
        ),
    ]
