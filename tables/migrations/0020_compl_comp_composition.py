# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0019_compl_comp_ammount'),
    ]

    operations = [
        migrations.AddField(
            model_name='compl_comp',
            name='composition',
            field=models.ForeignKey(blank=True, default=0, to='tables.Composition'),
            preserve_default=False,
        ),
    ]
