# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_auto_20170210_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='code',
            field=models.CharField(max_length=4, blank=True),
        ),
    ]
