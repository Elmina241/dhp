# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0044_auto_20170803_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='compAmount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='production',
            name='compUnit',
            field=models.ForeignKey(null=True, to='tables.Unit'),
        ),
    ]
