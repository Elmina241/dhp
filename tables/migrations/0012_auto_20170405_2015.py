# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0011_auto_20170405_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characteristic_set',
            name='characteristic_ptr',
        ),
        migrations.DeleteModel(
            name='Characteristic_set',
        ),
    ]
