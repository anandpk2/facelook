# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-18 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0009_auto_20160618_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cards',
            name='card_permision',
            field=models.CharField(choices=[('u', 'public'), ('o', 'private')], default='', max_length=1),
        ),
    ]