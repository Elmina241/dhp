# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0014_auto_20190226_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand_good',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
