# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0021_auto_20170523_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cap',
            field=models.ForeignKey(null=True, default=0, to='tables.Cap_group'),
        ),
        migrations.AddField(
            model_name='product',
            name='container',
            field=models.ForeignKey(null=True, default=0, to='tables.Container_group'),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='reactor',
            name='location',
            field=models.CharField(max_length=80, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reactor',
            name='product',
            field=models.CharField(max_length=250, default=1),
            preserve_default=False,
        ),
    ]
