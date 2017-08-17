# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0017_model_component_formula'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_component',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, default=None, to='processes.Batch'),
        ),
    ]
