# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_auto_20170203_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='ammount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
