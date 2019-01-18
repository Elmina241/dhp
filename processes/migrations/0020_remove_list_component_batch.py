# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0019_auto_20170822_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list_component',
            name='batch',
        ),
    ]
