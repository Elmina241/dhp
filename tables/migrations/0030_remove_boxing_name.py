# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0029_auto_20170731_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boxing',
            name='name',
        ),
    ]
