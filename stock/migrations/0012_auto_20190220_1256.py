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
            name='Counter_stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
        migrations.RemoveField(
            model_name='counterparty',
            name='category',
        ),
        migrations.AddField(
            model_name='counterparty',
            name='is_consumer',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='counterparty',
            name='is_member',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='counterparty',
            name='is_provider',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='counterparty',
            name='kind',
            field=models.CharField(max_length=20, choices=[('0', 'Организация'), ('1', 'Физлицо'), ('2', 'Административная группа')]),
        ),
        migrations.AlterField(
            model_name='stock',
            name='currency',
            field=models.ForeignKey(null=True, to='stock.Currency'),
        ),
        migrations.AddField(
            model_name='counter_stock',
            name='counter',
            field=models.ForeignKey(to='stock.Counterparty'),
        ),
        migrations.AddField(
            model_name='counter_stock',
            name='stock',
            field=models.ForeignKey(to='stock.Stock'),
        ),
    ]
