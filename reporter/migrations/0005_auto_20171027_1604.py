# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 13:04
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0004_auto_20171027_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Well',
            fields=[
                ('WID', models.AutoField(primary_key=True, serialize=False)),
                ('depth', models.CharField(max_length=10000)),
                ('avgwateryield', models.CharField(max_length=99999)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('FID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Farm')),
            ],
        ),
        migrations.DeleteModel(
            name='Incidences',
        ),
    ]
