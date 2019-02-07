# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
        ('stock', '0008_counterparty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good_name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('article', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('barcode', models.CharField(max_length=200)),
                ('original', models.CharField(max_length=200)),
                ('local', models.CharField(max_length=200)),
                ('transit', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Goods_unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('applicable', models.BooleanField()),
                ('isBase', models.BooleanField()),
                ('coeff', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='goods',
            name='base_unit',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='income_price',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='supply_price',
        ),
        migrations.AddField(
            model_name='goods',
            name='producer',
            field=models.ForeignKey(null=True, default=None, to='stock.Counterparty'),
        ),
        migrations.AddField(
            model_name='goods_property',
            name='editable',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods_property',
            name='visible',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods_unit',
            name='product',
            field=models.ForeignKey(to='stock.Goods'),
        ),
        migrations.AddField(
            model_name='goods_unit',
            name='unit',
            field=models.ForeignKey(to='tables.Unit'),
        ),
        migrations.AddField(
            model_name='good_name',
            name='product',
            field=models.ForeignKey(to='stock.Goods'),
        ),
    ]
