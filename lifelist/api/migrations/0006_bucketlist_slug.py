# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-21 18:28
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160821_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlist',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='title-slug-default', editable=False, populate_from=b'title'),
            preserve_default=False,
        ),
    ]