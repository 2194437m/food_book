# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodbookapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='com_body',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='com_recipe',
            new_name='recipe',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='com_user',
            new_name='user',
        ),
    ]
