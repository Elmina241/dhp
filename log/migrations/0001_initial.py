# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0024_mat_char_number_mat_char_var'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('mat', models.ForeignKey(to='tables.Material')),
            ],
        ),
    ]
