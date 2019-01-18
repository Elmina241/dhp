# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0028_auto_20170731_1458'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Container_form',
        ),
        migrations.AddField(
            model_name='container',
            name='form',
            field=models.CharField(max_length=80, default=0),
            preserve_default=False,
        ),
    ]
