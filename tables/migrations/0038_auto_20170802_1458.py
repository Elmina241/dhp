# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0037_compl_comp_form'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='product',
            name='option',
        ),
    ]
