# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0041_auto_20170802_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='production',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='production',
            field=models.OneToOneField(null=True, to='tables.Production'),
        ),
    ]
