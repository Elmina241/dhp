# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0050_auto_20170822_1636'),
        ('processes', '0021_auto_20170822_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_component',
            name='formula',
            field=models.ForeignKey(blank=True, null=True, default=None, to='tables.Formula'),
        ),
    ]
