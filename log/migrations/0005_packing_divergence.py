# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0028_auto_20171222_1559'),
        ('tables', '0052_auto_20180206_1103'),
        ('log', '0004_auto_20180206_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packing_divergence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start_amm', models.FloatField()),
                ('pack_amm', models.FloatField()),
                ('prod_num', models.FloatField()),
                ('batch', models.ForeignKey(to='processes.Batch')),
                ('product', models.ForeignKey(to='tables.Product')),
                ('reactor', models.ForeignKey(null=True, to='tables.Reactor')),
                ('tank', models.ForeignKey(null=True, to='tables.Tank')),
            ],
        ),
    ]
