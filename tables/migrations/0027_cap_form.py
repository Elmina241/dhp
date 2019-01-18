# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0026_remove_cap_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='cap',
            name='form',
            field=models.CharField(max_length=80, default=0),
            preserve_default=False,
        ),
    ]
