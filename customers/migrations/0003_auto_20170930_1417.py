# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20170929_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='contact_details',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]