# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20190117_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_group',
            name='parent',
        ),
    ]
