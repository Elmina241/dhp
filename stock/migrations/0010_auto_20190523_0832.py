# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_auto_20190508_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_operation',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
