# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0035_auto_20170731_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='form',
        ),
        migrations.AddField(
            model_name='composition',
            name='form',
            field=models.ForeignKey(null=True, to='tables.Product_form'),
        ),
    ]
