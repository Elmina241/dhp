# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0025_auto_20171025_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_component',
            name='max',
            field=models.FloatField(blank=True, null=True, default=None),
        ),
        migrations.AlterField(
            model_name='list_component',
            name='min',
            field=models.FloatField(blank=True, null=True, default=None),
        ),
    ]
