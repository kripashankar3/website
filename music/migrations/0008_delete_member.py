# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-08 10:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20171208_1534'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
    ]
