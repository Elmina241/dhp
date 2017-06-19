# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0021_auto_20170523_1210'),
        ('processes', '0009_auto_20170609_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model_component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ammount', models.FloatField()),
                ('compl', models.ForeignKey(blank=True, null=True, default=None, to='tables.Compl_comp')),
            ],
        ),
        migrations.CreateModel(
            name='Model_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('formula', models.ForeignKey(to='tables.Formula')),
            ],
        ),
        migrations.AddField(
            model_name='model_component',
            name='list',
            field=models.ForeignKey(to='processes.Model_list'),
        ),
        migrations.AddField(
            model_name='model_component',
            name='mat',
            field=models.ForeignKey(blank=True, null=True, default=None, to='tables.Material'),
        ),
    ]
