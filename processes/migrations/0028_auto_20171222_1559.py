# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0027_month_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month_plan',
            name='month',
            field=models.CharField(max_length=10),
        ),
    ]
