# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='default',
        ),
        migrations.RemoveField(
            model_name='property',
            name='editable',
        ),
        migrations.RemoveField(
            model_name='property',
            name='visible',
        ),
    ]
