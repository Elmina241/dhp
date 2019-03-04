# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0017_auto_20190304_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_good',
            name='cost',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
