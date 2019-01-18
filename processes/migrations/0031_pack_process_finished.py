# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0030_auto_20180711_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='pack_process',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
