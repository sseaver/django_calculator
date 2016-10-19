# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 20:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('number1', models.FloatField()),
                ('number2', models.FloatField()),
                ('function', models.CharField(max_length=1)),
                ('answer', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_level', models.CharField(choices=[('u', 'User'), ('o', 'Owner')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='operations',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]
