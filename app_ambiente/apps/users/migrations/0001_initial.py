# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUser',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('foto', models.ImageField(default=b'img/users/none.png', upload_to=b'img/users/', blank=True)),
                ('numero_celular', models.CharField(max_length=10, null=True, blank=True)),
                ('direccion', models.CharField(max_length=40, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='profileuser',
            name='type_profile',
            field=models.ForeignKey(to='users.TypeProfile'),
        ),
    ]
