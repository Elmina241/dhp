# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0024_kneading_isfinished'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_component',
            name='max',
            field=models.FloatField(blank=True, null=True, default=0),
        ),
        migrations.AddField(
            model_name='list_component',
            name='min',
            field=models.FloatField(blank=True, null=True, default=0),
        ),
    ]
