# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0029_model_list_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_list',
            name='time',
        ),
    ]
