# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0034_boxing_mat'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxing',
            name='group',
            field=models.ForeignKey(null=True, default=0, to='tables.Box_group'),
        ),
        migrations.AddField(
            model_name='boxing',
            name='mat',
            field=models.ForeignKey(null=True, default=0, to='tables.Boxing_mat'),
        ),
    ]
