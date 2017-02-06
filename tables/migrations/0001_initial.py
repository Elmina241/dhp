# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('mark', models.CharField(max_length=80)),
                ('concentration', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Material_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='group',
            field=models.ForeignKey(to='tables.Material_group'),
        ),
        migrations.AddField(
            model_name='material',
            name='prefix',
            field=models.ForeignKey(to='tables.Prefix'),
        ),
        migrations.AddField(
            model_name='material',
            name='unit',
            field=models.ForeignKey(to='tables.Unit'),
        ),
    ]
