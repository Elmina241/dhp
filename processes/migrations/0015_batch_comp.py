# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0046_auto_20170803_1220'),
        ('processes', '0014_auto_20170807_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch_comp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ammount', models.FloatField()),
                ('batch', models.ForeignKey(to='processes.Batch')),
                ('mat', models.ForeignKey(to='tables.Material')),
            ],
        ),
    ]
