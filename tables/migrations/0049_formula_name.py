# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0048_compl_comp_formula'),
    ]

    operations = [
        migrations.AddField(
            model_name='formula',
            name='name',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
