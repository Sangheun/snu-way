# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-10 02:32
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='detail_of_vehicle',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=blog.models.upload_location, width_field='width_field'),
        ),
    ]
