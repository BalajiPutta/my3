# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-25 08:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeformapp', '0009_employeemodels_etak'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeemodels',
            name='ebalaj',
        ),
        migrations.RemoveField(
            model_name='employeemodels',
            name='emastan',
        ),
        migrations.RemoveField(
            model_name='employeemodels',
            name='etak',
        ),
    ]