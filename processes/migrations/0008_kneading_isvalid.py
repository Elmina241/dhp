# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0007_batch_finish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='kneading',
            name='isValid',
            field=models.BooleanField(default=False),
        ),
    ]
