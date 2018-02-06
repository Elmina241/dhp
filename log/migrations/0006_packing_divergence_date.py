# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0005_packing_divergence'),
    ]

    operations = [
        migrations.AddField(
            model_name='packing_divergence',
            name='date',
            field=models.DateField(null=True, auto_now_add=True),
        ),
    ]
