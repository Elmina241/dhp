# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0028_auto_20171222_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_list',
            name='time',
            field=models.FloatField(blank=True, null=True, default=40),
        ),
    ]
