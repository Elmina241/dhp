# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0016_stock_good_stock_operation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_operation',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, to='stock.Stock'),
        ),
    ]
