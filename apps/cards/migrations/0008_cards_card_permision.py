# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-18 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_auto_20160529_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='card_permision',
            field=models.TextField(default=''),
        ),
    ]
