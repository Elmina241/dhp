# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0028_auto_20171222_1559'),
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movement_rec',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.FloatField(null=True)),
                ('date', models.DateField()),
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
        migrations.AddField(
            model_name='movement_rec',
            name='operation',
            field=models.ForeignKey(to='log.Operation'),
        ),
    ]
