# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 10:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodbookapp', '0028_auto_20170318_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='pictureLink',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='submitDate',
        ),
    ]