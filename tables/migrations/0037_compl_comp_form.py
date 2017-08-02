# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0036_auto_20170801_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='compl_comp',
            name='form',
            field=models.ForeignKey(blank=True, null=True, to='tables.Product_form'),
        ),
    ]
