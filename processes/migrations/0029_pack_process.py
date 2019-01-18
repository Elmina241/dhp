# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0057_auto_20180405_1240'),
        ('processes', '0028_auto_20171222_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pack_process',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('product', models.ForeignKey(to='tables.Product')),
                ('reactor', models.ForeignKey(to='tables.Reactor')),
                ('tank', models.ForeignKey(to='tables.Tank')),
            ],
        ),
    ]
