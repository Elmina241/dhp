# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0013_auto_20170214_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('min', models.FloatField()),
                ('max', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=80)),
                ('sgr', models.CharField(max_length=80)),
                ('group', models.ForeignKey(to='tables.Composition_group')),
            ],
        ),
        migrations.AddField(
            model_name='components',
            name='comp',
            field=models.ForeignKey(to='tables.Composition'),
        ),
        migrations.AddField(
            model_name='components',
            name='mat',
            field=models.ForeignKey(to='tables.Material'),
        ),
    ]
