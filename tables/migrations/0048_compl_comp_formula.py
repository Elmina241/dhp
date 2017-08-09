# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0047_remove_compl_comp_composition'),
    ]

    operations = [
        migrations.AddField(
            model_name='compl_comp',
            name='formula',
            field=models.ForeignKey(blank=True, null=True, default=None, to='tables.Formula'),
        ),
    ]
