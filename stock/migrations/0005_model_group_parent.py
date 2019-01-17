# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_remove_model_group_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_group',
            name='parent',
            field=models.IntegerField(null=True),
        ),
    ]
