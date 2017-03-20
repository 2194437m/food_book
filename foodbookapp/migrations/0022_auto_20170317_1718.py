# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodbookapp', '0021_auto_20170317_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='recipe',
            field=models.ManyToManyField(blank=True, related_name='recipe_tags', to='foodbookapp.Recipe'),
        ),
    ]