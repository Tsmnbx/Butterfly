# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfly', '0002_auto_20170929_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='Class_Name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
