# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ans', '0007_auto_20170915_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='answers_given',
            field=models.CharField(default='0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', max_length=200),
        ),
    ]