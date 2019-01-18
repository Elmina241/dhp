# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0024_mat_char_number_mat_char_var'),
    ]

    operations = [
        migrations.AddField(
            model_name='compl_comp',
            name='store_amount',
            field=models.FloatField(default=0),
        ),
    ]
