# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_remove_reactor_capacity'),
        ('processes', '0005_auto_20170227_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Batch_characteristic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('batch', models.ForeignKey(to='processes.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Formula_characteristic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kneading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('formula', models.ForeignKey(to='tables.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='State_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('kneading', models.ForeignKey(to='processes.Kneading')),
                ('state', models.ForeignKey(to='processes.State')),
            ],
        ),
        migrations.RemoveField(
            model_name='loading_list',
            name='date',
        ),
        migrations.CreateModel(
            name='Characteristic_number',
            fields=[
                ('characteristic_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='processes.Characteristic')),
                ('number', models.FloatField()),
            ],
            bases=('processes.characteristic',),
        ),
        migrations.CreateModel(
            name='Characteristic_range',
            fields=[
                ('characteristic_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='processes.Characteristic')),
                ('inf', models.FloatField()),
                ('sup', models.FloatField()),
            ],
            bases=('processes.characteristic',),
        ),
        migrations.CreateModel(
            name='Characteristic_set',
            fields=[
                ('characteristic_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='processes.Characteristic')),
                ('var_name', models.CharField(max_length=80)),
            ],
            bases=('processes.characteristic',),
        ),
        migrations.AddField(
            model_name='kneading',
            name='list',
            field=models.ForeignKey(to='processes.Loading_list'),
        ),
        migrations.AddField(
            model_name='formula_characteristic',
            name='characteristic',
            field=models.ForeignKey(to='processes.Characteristic'),
        ),
        migrations.AddField(
            model_name='formula_characteristic',
            name='formula',
            field=models.ForeignKey(to='tables.Formula'),
        ),
        migrations.AddField(
            model_name='characteristic',
            name='type',
            field=models.ForeignKey(to='processes.Characteristic_type'),
        ),
        migrations.AddField(
            model_name='batch_characteristic',
            name='characteristic',
            field=models.ForeignKey(to='processes.Characteristic'),
        ),
        migrations.AddField(
            model_name='batch',
            name='kneading',
            field=models.OneToOneField(to='processes.Kneading'),
        ),
    ]
