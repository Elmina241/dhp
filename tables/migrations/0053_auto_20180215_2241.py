# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0052_auto_20180206_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='composition',
            name='sh_life',
            field=models.IntegerField(default=24),
        ),
        migrations.AddField(
            model_name='composition',
            name='standard',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
