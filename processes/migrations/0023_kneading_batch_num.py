# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0022_list_component_formula'),
    ]

    operations = [
        migrations.AddField(
            model_name='kneading',
            name='batch_num',
            field=models.FloatField(default=0),
        ),
    ]
