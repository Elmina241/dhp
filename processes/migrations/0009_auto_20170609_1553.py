# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0021_auto_20170523_1210'),
        ('processes', '0008_kneading_isvalid'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_component',
            name='compl',
            field=models.ForeignKey(blank=True, null=True, default=None, to='tables.Compl_comp'),
        ),
        migrations.AlterField(
            model_name='list_component',
            name='mat',
            field=models.ForeignKey(blank=True, null=True, default=None, to='tables.Material'),
        ),
    ]
