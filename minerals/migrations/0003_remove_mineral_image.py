# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 17:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0002_auto_20170504_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mineral',
            name='image',
        ),
    ]
