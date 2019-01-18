# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0015_batch_comp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_component',
            name='compl',
        ),
    ]
