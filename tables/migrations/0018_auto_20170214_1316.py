# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0017_auto_20170214_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boxing',
            name='code',
        ),
        migrations.RemoveField(
            model_name='cap',
            name='code',
        ),
        migrations.RemoveField(
            model_name='container',
            name='code',
        ),
        migrations.RemoveField(
            model_name='sticker',
            name='code',
        ),
    ]
