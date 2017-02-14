# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0015_auto_20170214_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='composition',
            name='code',
        ),
    ]
