# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='bodegamaterial',
            name='peso',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='bodegamaterial',
            name='precio',
            field=models.DecimalField(null=True, max_digits=11, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='bodegamaterial',
            name='material',
            field=models.ForeignKey(to='solicitudes.TipoMaterial'),
        ),
        migrations.DeleteModel(
            name='Material',
        ),
    ]
