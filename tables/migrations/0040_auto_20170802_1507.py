# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0039_auto_20170802_1500'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_detail',
        ),
        migrations.DeleteModel(
            name='Product_option',
        ),
    ]
