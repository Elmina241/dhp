# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
        ('processes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acceptance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('mat', models.ForeignKey(to='tables.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Movement_rec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.FloatField(null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_printed', models.BooleanField(default=False)),
                ('batch', models.ForeignKey(null=True, to='processes.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Packaged',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.FloatField(null=True)),
                ('rec', models.ForeignKey(null=True, to='log.Movement_rec')),
            ],
        ),
        migrations.CreateModel(
            name='Packing_divergence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start_amm', models.FloatField()),
                ('pack_amm', models.FloatField()),
                ('date', models.DateField(null=True, auto_now_add=True)),
                ('prod_num', models.FloatField()),
                ('batch', models.ForeignKey(to='processes.Batch')),
                ('product', models.ForeignKey(to='tables.Product')),
                ('reactor', models.ForeignKey(null=True, to='tables.Reactor')),
                ('tank', models.ForeignKey(null=True, to='tables.Tank')),
            ],
        ),
        migrations.AddField(
            model_name='movement_rec',
            name='operation',
            field=models.ForeignKey(to='log.Operation'),
        ),
        migrations.AddField(
            model_name='movement_rec',
            name='product',
            field=models.ForeignKey(null=True, to='tables.Product'),
        ),
        migrations.AddField(
            model_name='acceptance',
            name='prod',
            field=models.ForeignKey(to='log.Movement_rec'),
        ),
    ]
