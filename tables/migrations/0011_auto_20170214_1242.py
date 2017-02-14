# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0010_auto_20170214_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='code',
            field=models.IntegerField(),
        ),
    ]
