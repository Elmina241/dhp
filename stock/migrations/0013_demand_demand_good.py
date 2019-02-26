# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
        ('stock', '0012_auto_20190220_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('release_date', models.DateField(null=True)),
                ('finish_date', models.DateField(null=True)),
                ('status', models.CharField(max_length=20, default='3', choices=[('0', 'Отказ'), ('1', 'Выполнение'), ('2', 'Закрыт'), ('3', 'Не рассмотрено')])),
                ('acceptor', models.ForeignKey(related_name='acceptor', to='stock.Stock')),
                ('consumer', models.ForeignKey(related_name='consumer', to='stock.Counterparty')),
                ('donor', models.ForeignKey(related_name='donor', to='stock.Stock')),
                ('provider', models.ForeignKey(related_name='provider', to='stock.Counterparty')),
            ],
        ),
        migrations.CreateModel(
            name='Demand_good',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=500)),
                ('amount', models.IntegerField(default=0)),
                ('demand', models.ForeignKey(to='stock.Demand')),
                ('good', models.ForeignKey(to='stock.Goods')),
                ('unit', models.ForeignKey(to='tables.Unit')),
            ],
        ),
    ]
