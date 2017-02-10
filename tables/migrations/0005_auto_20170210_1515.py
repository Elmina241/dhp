# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_auto_20170210_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composition_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='composition',
            name='group',
            field=models.ForeignKey(default=1, to='tables.Composition_group'),
            preserve_default=False,
        ),
    ]
