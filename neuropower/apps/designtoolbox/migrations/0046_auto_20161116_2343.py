# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-16 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designtoolbox', '0045_designmodel_seed'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodel',
            name='t_poststim',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='designmodel',
            name='t_prestim',
            field=models.FloatField(default=0),
        ),
    ]
