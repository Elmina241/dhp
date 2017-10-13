# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0023_kneading_batch_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='kneading',
            name='isFinished',
            field=models.BooleanField(default=False),
        ),
    ]
