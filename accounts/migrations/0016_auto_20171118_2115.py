# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20171112_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='house_number_name',
            field=models.CharField(max_length=40, verbose_name='House number/name'),
        ),
    ]
