# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 20:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tsadmsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tsadmsitedb',
            options={'verbose_name': 'Site', 'verbose_name_plural': 'Sites'},
        ),
    ]
