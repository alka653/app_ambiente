# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='key_user',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
    ]
