# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0013_remove_characteristic_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteristic',
            name='char_type',
            field=models.ForeignKey(default=1, to='tables.Characteristic_type'),
        ),
    ]
