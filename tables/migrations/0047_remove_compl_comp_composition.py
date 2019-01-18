# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0046_auto_20170803_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compl_comp',
            name='composition',
        ),
    ]
