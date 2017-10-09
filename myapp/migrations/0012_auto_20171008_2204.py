# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-08 16:34
from __future__ import unicode_literals

import cloudinary.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20171008_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downvote',
            name='question',
        ),
        migrations.RemoveField(
            model_name='downvote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='question',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='user',
        ),
        migrations.AlterField(
            model_name='question',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='downvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='question',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='upvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Downvote',
        ),
        migrations.DeleteModel(
            name='Upvote',
        ),
    ]