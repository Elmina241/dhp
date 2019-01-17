# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20190115_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_group',
            name='parent',
            field=models.IntegerField(null=True),
        ),
    ]
