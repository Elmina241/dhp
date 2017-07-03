# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0023_material_char'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mat_char_number',
            fields=[
                ('material_char_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Material_char')),
                ('number', models.FloatField()),
            ],
            bases=('tables.material_char',),
        ),
        migrations.CreateModel(
            name='Mat_char_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('char_var', models.ForeignKey(to='tables.Set_var')),
                ('mat_char', models.ForeignKey(to='tables.Material_char')),
            ],
        ),
    ]
