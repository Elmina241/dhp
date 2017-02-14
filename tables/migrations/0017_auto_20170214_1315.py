# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0016_remove_composition_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxing',
            name='code',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='cap',
            name='code',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='container',
            name='code',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='sticker',
            name='code',
            field=models.CharField(max_length=80),
        ),
    ]
