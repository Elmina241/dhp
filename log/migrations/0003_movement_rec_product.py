# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0051_composition_cur_batch'),
        ('log', '0002_auto_20180111_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='movement_rec',
            name='product',
            field=models.ForeignKey(null=True, to='tables.Product'),
        ),
    ]
