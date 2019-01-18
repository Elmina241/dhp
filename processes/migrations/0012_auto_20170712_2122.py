# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0011_reactor_content_tank_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reactor_content',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='reactor_content',
            name='kneading',
        ),
        migrations.RemoveField(
            model_name='reactor_content',
            name='reactor',
        ),
        migrations.RemoveField(
            model_name='tank_content',
            name='Tank',
        ),
        migrations.RemoveField(
            model_name='tank_content',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='tank_content',
            name='kneading',
        ),
        migrations.DeleteModel(
            name='Reactor_content',
        ),
        migrations.DeleteModel(
            name='Tank_content',
        ),
    ]
