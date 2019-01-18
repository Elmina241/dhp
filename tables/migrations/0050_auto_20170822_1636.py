# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0049_formula_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='compl_comp',
            name='reserved',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='material',
            name='reserved',
            field=models.FloatField(default=0),
        ),
    ]
