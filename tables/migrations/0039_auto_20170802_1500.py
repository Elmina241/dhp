# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0038_auto_20170802_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.CharField(max_length=80, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='option',
            field=models.CharField(max_length=80, default=0),
            preserve_default=False,
        ),
    ]
