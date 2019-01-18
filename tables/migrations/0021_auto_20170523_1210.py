# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0020_compl_comp_composition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compl_comp',
            name='composition',
            field=models.ForeignKey(blank=True, null=True, default=None, to='tables.Composition'),
        ),
    ]
