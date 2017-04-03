# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_remove_reactor_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic_set_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
            name='Set_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic_number',
            fields=[
                ('characteristic_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Characteristic')),
                ('number', models.FloatField()),
            ],
            bases=('tables.characteristic',),
        ),
        migrations.CreateModel(
            name='Characteristic_range',
            fields=[
                ('characteristic_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Characteristic')),
                ('inf', models.FloatField()),
                ('sup', models.FloatField()),
            ],
            bases=('tables.characteristic',),
        ),
        migrations.CreateModel(
            name='Characteristic_set',
            fields=[
                ('characteristic_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Characteristic')),
                ('set_name', models.CharField(max_length=80)),
            ],
            bases=('tables.characteristic',),
        ),
        migrations.AddField(
            model_name='formula_characteristic',
            name='characteristic',
            field=models.ForeignKey(to='tables.Characteristic'),
        ),
        migrations.AddField(
            model_name='formula_characteristic',
            name='formula',
            field=models.ForeignKey(to='tables.Formula'),
        ),
        migrations.AddField(
            model_name='characteristic_set_var',
            name='char_var',
            field=models.ForeignKey(to='tables.Set_var'),
        ),
        migrations.AddField(
            model_name='characteristic',
            name='type',
            field=models.ForeignKey(to='tables.Characteristic_type'),
        ),
        migrations.AddField(
            model_name='characteristic_set_var',
            name='char_set',
            field=models.ForeignKey(to='tables.Characteristic_set'),
        ),
    ]
