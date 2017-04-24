# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0006_auto_20170420_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='finish_date',
            field=models.DateField(default=datetime.datetime(2017, 4, 24, 2, 15, 32, 264376, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
