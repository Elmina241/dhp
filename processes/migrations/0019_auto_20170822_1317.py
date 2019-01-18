# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0018_list_component_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_component',
            name='r_cont',
            field=models.ForeignKey(blank=True, null=True, default=None, to='processes.Reactor_content'),
        ),
        migrations.AddField(
            model_name='list_component',
            name='t_cont',
            field=models.ForeignKey(blank=True, null=True, default=None, to='processes.Tank_content'),
        ),
    ]
