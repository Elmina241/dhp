# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0010_characteristic_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristic_set_var',
            name='char_set',
            field=models.ForeignKey(to='tables.Characteristic'),
        ),
    ]
