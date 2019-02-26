# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0013_demand_demand_good'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='acceptor',
            field=models.ForeignKey(null=True, related_name='acceptor', to='stock.Stock'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='donor',
            field=models.ForeignKey(null=True, related_name='donor', to='stock.Stock'),
        ),
    ]
