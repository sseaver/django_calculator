# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161019_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='access_level',
            field=models.CharField(choices=[('u', 'User'), ('o', 'Owner')], default='u', max_length=1),
        ),
    ]
