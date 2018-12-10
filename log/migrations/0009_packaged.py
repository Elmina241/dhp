# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0008_movement_rec_is_printed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packaged',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.FloatField(null=True)),
                ('rec', models.ForeignKey(null=True, to='log.Movement_rec')),
            ],
        ),
    ]
