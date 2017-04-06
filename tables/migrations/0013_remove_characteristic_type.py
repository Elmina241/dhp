# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0012_auto_20170405_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characteristic',
            name='type',
        ),
    ]
