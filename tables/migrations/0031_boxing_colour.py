# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0030_remove_boxing_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='boxing',
            name='colour',
            field=models.ForeignKey(null=True, default=0, to='tables.Colour'),
        ),
    ]
