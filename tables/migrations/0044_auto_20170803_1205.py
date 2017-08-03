# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0043_auto_20170802_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='production',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='production',
            name='weight',
        ),
    ]
