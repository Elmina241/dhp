# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0025_compl_comp_store_amount'),
        ('processes', '0010_auto_20170619_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reactor_content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('batch', models.ForeignKey(blank=True, null=True, default=None, to='processes.Batch')),
                ('kneading', models.ForeignKey(blank=True, null=True, default=None, to='processes.Kneading')),
                ('reactor', models.ForeignKey(to='tables.Reactor')),
            ],
        ),
        migrations.CreateModel(
            name='Tank_content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('Tank', models.ForeignKey(to='tables.Tank')),
                ('batch', models.ForeignKey(blank=True, null=True, default=None, to='processes.Batch')),
                ('kneading', models.ForeignKey(blank=True, null=True, default=None, to='processes.Kneading')),
            ],
        ),
    ]
