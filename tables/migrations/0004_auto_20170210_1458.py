# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_material_ammount'),
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
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=80)),
                ('sgr', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
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
