# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_auto_20170216_2000'),
        ('processes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loading_list',
            name='name',
        ),
        migrations.AddField(
            model_name='loading_list',
            name='composition',
            field=models.ForeignKey(default=1, to='tables.Composition'),
            preserve_default=False,
        ),
    ]
