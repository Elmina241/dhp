# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0006_packing_divergence_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acceptance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('prod', models.ForeignKey(to='log.Movement_rec')),
            ],
        ),
    ]
