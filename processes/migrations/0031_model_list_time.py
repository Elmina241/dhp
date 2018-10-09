# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0030_remove_model_list_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_list',
            name='time',
            field=models.IntegerField(null=True, default=40),
        ),
    ]
