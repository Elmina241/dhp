# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0056_auto_20180319_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comp_prop',
            name='characteristic',
            field=models.ForeignKey(to='tables.Composition_char'),
        ),
    ]
