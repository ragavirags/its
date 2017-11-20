# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 08:24
from __future__ import unicode_literals

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counties', models.CharField(max_length=25)),
                ('codes', models.IntegerField()),
                ('cty_code', models.CharField(max_length=24)),
                ('dis', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='Crops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Rice', max_length=50)),
                ('Year', models.IntegerField()),
                ('Seasons', models.CharField(choices=[('S', 'Summer'), ('W', 'Winter'), ('M', 'Monsoon')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Farms',
            fields=[
                ('FID', models.AutoField(primary_key=True, serialize=False)),
                ('plot', django.contrib.gis.db.models.fields.PolygonField(geography=True, srid=4326)),
                ('area', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('name', models.CharField(max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('HID', models.AutoField(primary_key=True, serialize=False)),
                ('income', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Incidences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': ' Incidences',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('PID', models.AutoField(primary_key=True, serialize=False)),
                ('Age', models.IntegerField(default=0)),
                ('Name', models.CharField(default='', max_length=30)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('HID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Houses')),
            ],
        ),
        migrations.CreateModel(
            name='Yields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Yield', models.FloatField(default=0.0)),
                ('measured_date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.AddField(
            model_name='farms',
            name='HID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Houses'),
        ),
        migrations.AddField(
            model_name='crops',
            name='FID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Farms'),
        ),
    ]
