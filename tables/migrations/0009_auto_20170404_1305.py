# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0008_auto_20170403_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characteristic_number',
            name='characteristic_ptr',
        ),
        migrations.DeleteModel(
            name='Characteristic_number',
        ),
    ]
