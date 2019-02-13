# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_closed', models.BooleanField()),
                ('finish_date', models.DateField(null=True)),
                ('status', models.CharField(max_length=20, choices=[('0', 'Не рассмотренно'), ('1', 'Одобрено'), ('2', 'Отвергнуто')])),
                ('base', models.ForeignKey(to='stock.Base')),
                ('consumer', models.ForeignKey(to='stock.Counterparty')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=500)),
                ('group', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='demand',
            name='signer',
            field=models.ForeignKey(to='stock.User'),
        ),
        migrations.AddField(
            model_name='demand',
            name='stock',
            field=models.ForeignKey(to='stock.Stock'),
        ),
    ]
