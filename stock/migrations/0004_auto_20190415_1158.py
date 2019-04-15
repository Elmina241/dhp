# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20190404_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='counterparty',
            name='cur_vin',
            field=models.IntegerField(blank=True, default='0'),
        ),
        migrations.AddField(
            model_name='demand',
            name='vin',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='cur_vin',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='stock_operation',
            name='vin',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
