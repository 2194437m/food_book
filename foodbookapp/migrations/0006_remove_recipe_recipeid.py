# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 23:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodbookapp', '0005_remove_recipe_favouritedby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipeID',
        ),
    ]