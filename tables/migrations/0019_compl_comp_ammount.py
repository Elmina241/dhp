# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0018_compl_comp_compl_comp_comp'),
    ]

    operations = [
        migrations.AddField(
            model_name='compl_comp',
            name='ammount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
