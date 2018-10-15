# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0007_acceptance'),
    ]

    operations = [
        migrations.AddField(
            model_name='movement_rec',
            name='is_printed',
            field=models.BooleanField(default=False),
        ),
    ]
