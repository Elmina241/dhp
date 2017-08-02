# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0042_auto_20170802_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.AddField(
            model_name='production',
            name='unit',
            field=models.ForeignKey(null=True, to='tables.Unit'),
        ),
        migrations.AddField(
            model_name='production',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
