# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 16:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodbookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipeText',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='tagTitle',
            field=models.CharField(default='', max_length=128, unique=True),
        ),
    ]
