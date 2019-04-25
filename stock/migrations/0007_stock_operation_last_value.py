# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_demand_is_demand'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_operation',
            name='last_value',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
