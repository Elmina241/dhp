# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_auto_20190523_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
