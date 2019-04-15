# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20190415_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='is_demand',
            field=models.BooleanField(default=True),
        ),
    ]
