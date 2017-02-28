# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_auto_20170216_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('composition', models.ForeignKey(to='tables.Composition')),
            ],
        ),
        migrations.CreateModel(
            name='Formula_component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ammount', models.FloatField()),
                ('formula', models.ForeignKey(to='tables.Formula')),
                ('mat', models.ForeignKey(to='tables.Material')),
            ],
        ),
    ]
