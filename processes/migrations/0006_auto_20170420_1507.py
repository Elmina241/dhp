# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0015_auto_20170407_1151'),
        ('processes', '0005_auto_20170331_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kneading_char',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kneading_char_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('char_var', models.ForeignKey(to='tables.Set_var')),
            ],
        ),
        migrations.CreateModel(
            name='Kneading_char_number',
            fields=[
                ('kneading_char_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='processes.Kneading_char')),
                ('number', models.FloatField()),
            ],
            bases=('processes.kneading_char',),
        ),
        migrations.AddField(
            model_name='kneading_char_var',
            name='kneading_char',
            field=models.ForeignKey(to='processes.Kneading_char'),
        ),
        migrations.AddField(
            model_name='kneading_char',
            name='characteristic',
            field=models.ForeignKey(to='tables.Characteristic'),
        ),
        migrations.AddField(
            model_name='kneading_char',
            name='kneading',
            field=models.ForeignKey(to='processes.Kneading'),
        ),
    ]
