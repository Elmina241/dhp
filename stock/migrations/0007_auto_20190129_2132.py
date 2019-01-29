# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20190122_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Default_number',
            fields=[
                ('model_property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Model_property')),
                ('number', models.FloatField()),
            ],
            bases=('stock.model_property',),
        ),
        migrations.CreateModel(
            name='Default_text',
            fields=[
                ('model_property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Model_property')),
                ('text', models.CharField(max_length=200)),
            ],
            bases=('stock.model_property',),
        ),
        migrations.CreateModel(
            name='Default_var',
            fields=[
                ('model_property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Model_property')),
                ('var', models.ForeignKey(to='stock.Property_var')),
            ],
            bases=('stock.model_property',),
        ),
        migrations.RemoveField(
            model_name='property_string',
            name='property_ptr',
        ),
        migrations.DeleteModel(
            name='Property_string',
        ),
    ]
