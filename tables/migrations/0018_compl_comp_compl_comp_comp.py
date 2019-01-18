# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0017_auto_20170511_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compl_comp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Compl_comp_comp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ammount', models.FloatField()),
                ('compl', models.ForeignKey(to='tables.Compl_comp')),
                ('mat', models.ForeignKey(to='tables.Material')),
            ],
        ),
    ]
