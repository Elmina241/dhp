# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0004_loading_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loading_list',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
