# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0031_boxing_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxing',
            name='form',
            field=models.CharField(max_length=80, default=0),
            preserve_default=False,
        ),
    ]
