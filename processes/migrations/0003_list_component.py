# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_auto_20170216_2000'),
        ('processes', '0002_auto_20170221_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='List_component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ammount', models.FloatField()),
                ('list', models.ForeignKey(to='processes.Loading_list')),
                ('mat', models.ForeignKey(to='tables.Material')),
            ],
        ),
    ]
