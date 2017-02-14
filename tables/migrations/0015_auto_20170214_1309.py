# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0014_auto_20170214_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='code',
            field=models.CharField(max_length=11),
        ),
    ]
