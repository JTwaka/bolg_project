# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 14:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArticleManager',
        ),
    ]
