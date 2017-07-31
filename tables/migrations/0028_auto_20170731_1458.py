# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0027_cap_form'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cap_form',
        ),
        migrations.RemoveField(
            model_name='container',
            name='form',
        ),
    ]
