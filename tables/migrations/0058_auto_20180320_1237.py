# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0057_auto_20180320_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comp_prop',
            name='characteristic',
        ),
        migrations.RemoveField(
            model_name='comp_prop_number',
            name='comp_prop_ptr',
        ),
        migrations.AddField(
            model_name='comp_prop_number',
            name='composition_char_ptr',
            field=models.OneToOneField(primary_key=True, default=0, serialize=False, auto_created=True, parent_link=True, to='tables.Composition_char'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comp_prop_var',
            name='comp_prop',
            field=models.ForeignKey(to='tables.Composition_char'),
        ),
        migrations.DeleteModel(
            name='Comp_prop',
        ),
    ]
