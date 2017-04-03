# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0007_auto_20170331_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Char_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='characteristic',
            name='group',
            field=models.ForeignKey(default=1, to='tables.Char_group'),
            preserve_default=False,
        ),
    ]
