# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiler', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPageGalleryImage',
            new_name='ProfilePageGalleryImage',
        ),
    ]
