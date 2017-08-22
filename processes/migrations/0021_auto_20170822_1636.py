# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0020_remove_list_component_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactor_content',
            name='reserved',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='tank_content',
            name='reserved',
            field=models.FloatField(default=0),
        ),
    ]
