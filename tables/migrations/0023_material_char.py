# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0022_auto_20170625_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material_char',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('characteristic', models.ForeignKey(to='tables.Characteristic')),
                ('mat', models.ForeignKey(to='tables.Material')),
            ],
        ),
    ]
