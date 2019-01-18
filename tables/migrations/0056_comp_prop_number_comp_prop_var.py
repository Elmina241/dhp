# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0055_characteristic_is_general'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comp_prop_number',
            fields=[
                ('composition_char_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Composition_char')),
                ('number', models.FloatField()),
            ],
            bases=('tables.composition_char',),
        ),
        migrations.CreateModel(
            name='Comp_prop_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('char_var', models.ForeignKey(to='tables.Set_var')),
                ('comp_prop', models.ForeignKey(to='tables.Composition_char')),
            ],
        ),
    ]
