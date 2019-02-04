# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20190129_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counterparty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('kind', models.CharField(max_length=20, choices=[('0', 'Организация'), ('1', 'Физлицо'), ('2', 'Предприниматель'), ('3', 'Подразделение')])),
                ('category', models.CharField(max_length=20, choices=[('0', 'Поставщик'), ('1', 'Потребитель'), ('2', 'Смешанный'), ('3', 'Информационный')])),
            ],
        ),
    ]
