# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0004_kneading_reactor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characteristic',
            name='type',
        ),
        migrations.RemoveField(
            model_name='characteristic_number',
            name='characteristic_ptr',
        ),
        migrations.RemoveField(
            model_name='characteristic_range',
            name='characteristic_ptr',
        ),
        migrations.RemoveField(
            model_name='characteristic_set',
            name='characteristic_ptr',
        ),
        migrations.RemoveField(
            model_name='formula_characteristic',
            name='characteristic',
        ),
        migrations.RemoveField(
            model_name='formula_characteristic',
            name='formula',
        ),
        migrations.RemoveField(
            model_name='batch_characteristic',
            name='characteristic',
        ),
        migrations.AlterField(
            model_name='kneading',
            name='reactor',
            field=models.ForeignKey(to='tables.Reactor'),
        ),
        migrations.DeleteModel(
            name='Characteristic',
        ),
        migrations.DeleteModel(
            name='Characteristic_number',
        ),
        migrations.DeleteModel(
            name='Characteristic_range',
        ),
        migrations.DeleteModel(
            name='Characteristic_set',
        ),
        migrations.DeleteModel(
            name='Characteristic_type',
        ),
        migrations.DeleteModel(
            name='Formula_characteristic',
        ),
    ]
