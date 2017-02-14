# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0018_auto_20170214_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxing',
            name='code',
            field=models.CharField(max_length=80, default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cap',
            name='code',
            field=models.CharField(max_length=80, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='composition',
            name='code',
            field=models.CharField(max_length=4, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='container',
            name='code',
            field=models.CharField(max_length=80, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sticker',
            name='code',
            field=models.CharField(max_length=80, default=1),
            preserve_default=False,
        ),
    ]
