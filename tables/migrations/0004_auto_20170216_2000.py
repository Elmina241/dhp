# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_production_reactor_tank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cap',
            name='name',
        ),
        migrations.RemoveField(
            model_name='container',
            name='name',
        ),
    ]
