# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0003_list_component'),
    ]

    operations = [
        migrations.AddField(
            model_name='loading_list',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 2, 21, 3, 6, 32, 880552, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
