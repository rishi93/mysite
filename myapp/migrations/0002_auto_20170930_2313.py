# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-30 17:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 30, 17, 43, 31, 713603, tzinfo=utc)),
        ),
    ]
