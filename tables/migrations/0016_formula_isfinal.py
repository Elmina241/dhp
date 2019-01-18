# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0015_auto_20170407_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='formula',
            name='isFinal',
            field=models.BooleanField(default=True),
        ),
    ]
