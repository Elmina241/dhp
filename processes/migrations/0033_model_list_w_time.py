# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0032_remove_model_list_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_list',
            name='w_time',
            field=models.IntegerField(default=40),
        ),
    ]
