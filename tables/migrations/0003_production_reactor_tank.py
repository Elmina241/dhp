# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_auto_20170215_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('boxing', models.ForeignKey(to='tables.Boxing')),
                ('cap', models.ForeignKey(to='tables.Cap')),
                ('composition', models.ForeignKey(to='tables.Composition')),
                ('container', models.ForeignKey(to='tables.Container')),
                ('product', models.ForeignKey(to='tables.Product')),
                ('sticker', models.ForeignKey(to='tables.Sticker')),
            ],
        ),
        migrations.CreateModel(
            name='Reactor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('capacity', models.FloatField()),
                ('min', models.FloatField()),
                ('max', models.FloatField()),
                ('ready', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('capacity', models.FloatField()),
                ('ready', models.BooleanField()),
            ],
        ),
    ]
