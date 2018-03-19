# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0055_characteristic_is_general'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comp_prop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comp_prop_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('char_var', models.ForeignKey(to='tables.Set_var')),
            ],
        ),
        migrations.CreateModel(
            name='Comp_prop_number',
            fields=[
                ('comp_prop_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Comp_prop')),
                ('number', models.FloatField()),
            ],
            bases=('tables.comp_prop',),
        ),
        migrations.AddField(
            model_name='comp_prop_var',
            name='comp_prop',
            field=models.ForeignKey(to='tables.Comp_prop'),
        ),
        migrations.AddField(
            model_name='comp_prop',
            name='characteristic',
            field=models.ForeignKey(to='tables.Characteristic'),
        ),
    ]
