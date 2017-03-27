# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0004_kneading_reactor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kneading',
            name='reactor',
            field=models.ForeignKey(to='tables.Reactor'),
        ),
    ]
