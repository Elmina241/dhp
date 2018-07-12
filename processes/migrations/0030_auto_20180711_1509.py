# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0029_pack_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack_process',
            name='reactor',
            field=models.ForeignKey(null=True, to='tables.Reactor'),
        ),
        migrations.AlterField(
            model_name='pack_process',
            name='tank',
            field=models.ForeignKey(null=True, to='tables.Tank'),
        ),
    ]
