# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0007_auto_20170330_2142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic_set_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Set_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.RenameField(
            model_name='characteristic_set',
            old_name='var_name',
            new_name='set_name',
        ),
        migrations.AddField(
            model_name='characteristic_set_var',
            name='char_set',
            field=models.ForeignKey(to='tables.Characteristic_set'),
        ),
        migrations.AddField(
            model_name='characteristic_set_var',
            name='char_var',
            field=models.ForeignKey(to='tables.Set_var'),
        ),
    ]
