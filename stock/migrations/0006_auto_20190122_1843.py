# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_model_group_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_unit',
            name='coeff',
        ),
        migrations.RemoveField(
            model_name='model_unit',
            name='is_base',
        ),
        migrations.AddField(
            model_name='model_property',
            name='editable',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model_property',
            name='isDefault',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model_property',
            name='visible',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
