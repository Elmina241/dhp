# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_movement_rec_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement_rec',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
