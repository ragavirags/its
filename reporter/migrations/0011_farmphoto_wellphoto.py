# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0010_housephoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmphoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.FileField(blank=True, null=True, upload_to='')),
                ('FarmID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Farm')),
            ],
        ),
        migrations.CreateModel(
            name='Wellphoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.FileField(blank=True, null=True, upload_to='')),
                ('WellID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Well')),
            ],
        ),
    ]
