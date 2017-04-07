# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0014_characteristic_char_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comp_char_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('char_var', models.ForeignKey(to='tables.Set_var')),
            ],
        ),
        migrations.CreateModel(
            name='Composition_char',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='formula_characteristic',
            name='characteristic',
        ),
        migrations.RemoveField(
            model_name='formula_characteristic',
            name='formula',
        ),
        migrations.CreateModel(
            name='Comp_char_number',
            fields=[
                ('composition_char_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Composition_char')),
                ('number', models.FloatField()),
            ],
            bases=('tables.composition_char',),
        ),
        migrations.CreateModel(
            name='Comp_char_range',
            fields=[
                ('composition_char_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Composition_char')),
                ('inf', models.FloatField()),
                ('sup', models.FloatField()),
            ],
            bases=('tables.composition_char',),
        ),
        migrations.DeleteModel(
            name='Formula_characteristic',
        ),
        migrations.AddField(
            model_name='composition_char',
            name='characteristic',
            field=models.ForeignKey(to='tables.Characteristic'),
        ),
        migrations.AddField(
            model_name='composition_char',
            name='comp',
            field=models.ForeignKey(to='tables.Composition'),
        ),
        migrations.AddField(
            model_name='comp_char_var',
            name='comp_char',
            field=models.ForeignKey(to='tables.Composition_char'),
        ),
    ]
