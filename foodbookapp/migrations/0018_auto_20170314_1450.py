# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodbookapp', '0017_auto_20170312_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commentBody',
            new_name='comment_body',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commentedBy',
            new_name='commented_by',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commentedOn',
            new_name='commented_on',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='favouritedBy',
            new_name='favourited_ny',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='pictureLink',
            new_name='picture_link',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipeText',
            new_name='recipe_text',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='submitDate',
            new_name='submit_date',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='submittedBy',
            new_name='submitted_by',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='userID',
        ),
    ]
