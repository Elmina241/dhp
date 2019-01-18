# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0009_auto_20170404_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic_number',
            fields=[
                ('characteristic_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Characteristic')),
                ('inf', models.FloatField()),
                ('sup', models.FloatField()),
            ],
            bases=('tables.characteristic',),
        ),
    ]
