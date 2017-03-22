# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0002_remove_kneading_formula'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_component',
            name='loaded',
            field=models.BooleanField(default=False),
        ),
    ]
