# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0056_comp_prop_number_comp_prop_var'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='certificate',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='composition',
            name='declaration',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
