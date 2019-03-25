# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20190325_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_operation',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
