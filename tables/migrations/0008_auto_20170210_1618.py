# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0007_auto_20170210_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='code',
            field=models.IntegerField(max_length=4, blank=True),
        ),
    ]
