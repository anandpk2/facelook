# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 09:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cards',
            old_name='card_created_on',
            new_name='card_created',
        ),
    ]
