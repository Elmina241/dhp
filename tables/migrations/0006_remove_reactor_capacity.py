# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0005_formula_formula_component'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reactor',
            name='capacity',
        ),
    ]
