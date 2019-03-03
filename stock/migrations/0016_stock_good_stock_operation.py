# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
        ('stock', '0015_demand_good_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_good',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.IntegerField(default=0)),
                ('cost', models.FloatField(default=0)),
                ('good', models.ForeignKey(to='stock.Goods')),
                ('stock', models.ForeignKey(to='stock.Stock')),
                ('unit', models.ForeignKey(to='tables.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_operation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('operation', models.CharField(max_length=20, default='0', choices=[('0', 'Приход'), ('1', 'Расход'), ('2', 'Коррекция')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cause', models.CharField(max_length=20, default='0', choices=[('0', 'Перемещение'), ('1', 'Оприходование'), ('2', 'Выбытие'), ('3', 'Инвентаризация')])),
                ('cause_id', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('cost', models.FloatField(blank=True, default=0)),
                ('good', models.ForeignKey(to='stock.Goods')),
                ('stock', models.ForeignKey(blank=True, to='stock.Stock')),
                ('unit', models.ForeignKey(to='tables.Unit')),
            ],
        ),
    ]
