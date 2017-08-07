# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0013_reactor_content_tank_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch_characteristic',
            name='batch',
        ),
        migrations.DeleteModel(
            name='Batch_characteristic',
        ),
    ]
