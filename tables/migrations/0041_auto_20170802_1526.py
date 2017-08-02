# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0040_auto_20170802_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cap',
        ),
        migrations.RemoveField(
            model_name='product',
            name='container',
        ),
    ]
