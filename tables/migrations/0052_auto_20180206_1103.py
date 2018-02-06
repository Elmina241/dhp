# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0051_composition_cur_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='formula',
            name='cur_batch',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='composition',
            name='cur_batch',
            field=models.FloatField(default=1),
        ),
    ]
