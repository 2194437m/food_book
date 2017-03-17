# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodbookapp', '0025_auto_20170317_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='recipe_tags', to='foodbookapp.Tag'),
        ),
    ]
