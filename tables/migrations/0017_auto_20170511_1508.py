# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0016_formula_isfinal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formula',
            name='isFinal',
        ),
        migrations.AddField(
            model_name='composition',
            name='isFinal',
            field=models.BooleanField(default=True),
        ),
    ]
