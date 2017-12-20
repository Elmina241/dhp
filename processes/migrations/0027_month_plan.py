# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0051_composition_cur_batch'),
        ('processes', '0026_auto_20171026_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month_plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('month', models.CharField(max_length=7)),
                ('num', models.FloatField()),
                ('prod', models.ForeignKey(to='tables.Product')),
            ],
        ),
    ]
