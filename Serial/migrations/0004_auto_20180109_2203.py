# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-09 22:03
from __future__ import unicode_literals

import Serial.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serial', '0003_auto_20180109_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=Serial.models.user_directory_path),
        ),
    ]
