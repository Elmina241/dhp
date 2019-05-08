# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_demand_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='consumer',
            field=models.ForeignKey(null=True, related_name='consumer', to='stock.Counterparty'),
        ),
        migrations.AlterField(
            model_name='demand',
            name='provider',
            field=models.ForeignKey(null=True, related_name='provider', to='stock.Counterparty'),
        ),
    ]
