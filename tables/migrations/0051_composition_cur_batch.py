# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0050_auto_20170822_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='cur_batch',
            field=models.FloatField(default=0),
        ),
    ]
