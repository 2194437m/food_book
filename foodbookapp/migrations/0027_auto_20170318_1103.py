# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodbookapp', '0026_auto_20170317_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='com_recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_comments', to='foodbookapp.Recipe'),
        ),
    ]
