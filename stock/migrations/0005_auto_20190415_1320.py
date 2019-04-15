# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20190415_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_operation',
            name='vin',
        ),
        migrations.AddField(
            model_name='package',
            name='vin',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
