# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-12 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0014_auto_20161112_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='salary',
            field=models.CharField(default=-4, max_length=20),
            preserve_default=False,
        ),
    ]
