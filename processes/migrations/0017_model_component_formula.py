# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0049_formula_name'),
        ('processes', '0016_remove_model_component_compl'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_component',
            name='formula',
            field=models.ForeignKey(blank=True, null=True, default=None, to='tables.Formula'),
        ),
    ]
