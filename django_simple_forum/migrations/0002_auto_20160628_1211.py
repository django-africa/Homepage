# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumcategory',
            name='slug',
            field=models.SlugField(default='test', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(default='test', max_length=1000),
            preserve_default=False,
        ),
    ]
