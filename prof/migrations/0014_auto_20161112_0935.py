# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-12 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0013_jobs_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='experience',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='location',
            field=models.CharField(default='Bangalore', max_length=100),
            preserve_default=False,
        ),
    ]
