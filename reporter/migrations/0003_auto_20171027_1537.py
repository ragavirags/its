# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 12:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0002_houses_noofmem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Houses',
            new_name='House',
        ),
        migrations.RenameModel(
            old_name='Members',
            new_name='Household',
        ),
    ]
