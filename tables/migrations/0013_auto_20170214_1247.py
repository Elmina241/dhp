# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0012_auto_20170214_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='components',
            name='comp',
        ),
        migrations.RemoveField(
            model_name='components',
            name='mat',
        ),
        migrations.RemoveField(
            model_name='composition',
            name='group',
        ),
        migrations.DeleteModel(
            name='Components',
        ),
        migrations.DeleteModel(
            name='Composition',
        ),
    ]
