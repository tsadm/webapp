# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tsadmsite', '0004_auto_20160303_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tsadmsiteenvdb',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
