# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-22 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NeuropowerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SID', models.CharField(default='', max_length=300)),
                ('step', models.IntegerField(default=0)),
                ('map_url', models.URLField(default='')),
                ('mask_url', models.URLField(default='')),
                ('map_local', models.CharField(default='', max_length=300)),
                ('mask_local', models.CharField(default='', max_length=300)),
                ('peaktable', picklefield.fields.PickledObjectField(default='', editable=False)),
                ('location', models.CharField(default='', max_length=300)),
                ('spmfile', models.FileField(default='', upload_to='/maps')),
                ('masklocation', models.CharField(default='', max_length=300)),
                ('maskfile', models.FileField(default='', upload_to='/maps')),
                ('nvox', models.CharField(default='', max_length=300)),
                ('ZorT', models.CharField(choices=[('Z', 'Z'), ('T', 'T')], max_length=10)),
                ('Exc', models.FloatField(blank=True, null=True)),
                ('ExcZ', models.FloatField(blank=True, null=True)),
                ('DoF', models.FloatField(blank=True, null=True)),
                ('Subj', models.IntegerField()),
                ('alpha', models.FloatField(blank=True, null=True)),
                ('Samples', models.IntegerField(choices=[(1, 'One-sample'), (2, 'Two-sample')])),
                ('SmoothEst', models.IntegerField(choices=[(1, 'Manual'), (2, 'Estimate')], default=1)),
                ('Smoothx', models.FloatField(blank=True, null=True)),
                ('Smoothy', models.FloatField(blank=True, null=True)),
                ('Smoothz', models.FloatField(blank=True, null=True)),
                ('Voxx', models.FloatField(blank=True, null=True)),
                ('Voxy', models.FloatField(blank=True, null=True)),
                ('Voxz', models.FloatField(blank=True, null=True)),
                ('err', models.CharField(default='', max_length=1000)),
                ('pi1', models.FloatField(blank=True, null=True)),
                ('a', models.FloatField(blank=True, null=True)),
                ('mu', models.FloatField(blank=True, null=True)),
                ('sigma', models.FloatField(blank=True, null=True)),
                ('data', picklefield.fields.PickledObjectField(default='', editable=False)),
                ('reqPow', models.FloatField(blank=True, null=True)),
                ('reqSS', models.IntegerField(blank=True, null=True)),
                ('MCP', models.CharField(choices=[('RFT', 'Random Field Theory'), ('BH', 'Benjamini-Hochberg'), ('BF', 'Bonferroni'), ('UN', 'Uncorrected')], max_length=10)),
            ],
        ),
    ]
