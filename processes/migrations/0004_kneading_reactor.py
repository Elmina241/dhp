# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0006_remove_reactor_capacity'),
        ('processes', '0003_list_component_loaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='kneading',
            name='reactor',
            field=models.ForeignKey(default=4, to='tables.Reactor'),
        ),
    ]
