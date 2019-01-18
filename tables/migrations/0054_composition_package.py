# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0053_auto_20180215_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='package',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
