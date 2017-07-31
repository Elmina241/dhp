# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0025_compl_comp_store_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cap',
            name='form',
        ),
    ]
