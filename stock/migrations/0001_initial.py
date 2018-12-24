# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('supply_price', models.FloatField()),
                ('income_price', models.FloatField()),
                ('base_unit', models.ForeignKey(to='tables.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Goods_property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('applicable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Model_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(null=True, to='stock.Model_group')),
            ],
        ),
        migrations.CreateModel(
            name='Model_property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model_unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('coeff', models.FloatField()),
                ('is_base', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('group', models.ForeignKey(to='stock.Model_group')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('prop_type', models.PositiveSmallIntegerField()),
                ('visible', models.BooleanField()),
                ('editable', models.BooleanField()),
                ('default', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Goods_string',
            fields=[
                ('goods_property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Goods_property')),
                ('text', models.CharField(max_length=500)),
            ],
            bases=('stock.goods_property',),
        ),
        migrations.CreateModel(
            name='Goods_var',
            fields=[
                ('goods_property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Goods_property')),
            ],
            bases=('stock.goods_property',),
        ),
        migrations.CreateModel(
            name='Property_num',
            fields=[
                ('goods_property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Goods_property')),
                ('number', models.FloatField()),
            ],
            bases=('stock.goods_property',),
        ),
        migrations.CreateModel(
            name='Property_range',
            fields=[
                ('property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Property')),
                ('inf', models.FloatField()),
                ('sup', models.FloatField()),
            ],
            bases=('stock.property',),
        ),
        migrations.CreateModel(
            name='Property_string',
            fields=[
                ('property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Property')),
                ('text', models.CharField(max_length=500)),
            ],
            bases=('stock.property',),
        ),
        migrations.AddField(
            model_name='property_var',
            name='prop',
            field=models.ForeignKey(to='stock.Property'),
        ),
        migrations.AddField(
            model_name='model_unit',
            name='model',
            field=models.ForeignKey(to='stock.Product_model'),
        ),
        migrations.AddField(
            model_name='model_unit',
            name='unit',
            field=models.ForeignKey(to='tables.Unit'),
        ),
        migrations.AddField(
            model_name='model_property',
            name='model',
            field=models.ForeignKey(to='stock.Product_model'),
        ),
        migrations.AddField(
            model_name='model_property',
            name='prop',
            field=models.ForeignKey(to='stock.Property'),
        ),
        migrations.AddField(
            model_name='goods_property',
            name='product',
            field=models.ForeignKey(to='stock.Goods'),
        ),
        migrations.AddField(
            model_name='goods_property',
            name='property',
            field=models.ForeignKey(to='stock.Property'),
        ),
        migrations.AddField(
            model_name='goods',
            name='model',
            field=models.ForeignKey(to='stock.Product_model'),
        ),
        migrations.AddField(
            model_name='goods_var',
            name='var',
            field=models.ForeignKey(to='stock.Property_var'),
        ),
    ]
