# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 16:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodbookapp', '0018_auto_20170314_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='favourited_ny',
            new_name='favourited_by',
        ),
    ]
