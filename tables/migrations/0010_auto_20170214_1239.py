# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0009_auto_20170210_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boxing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.IntegerField(blank=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Cap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.IntegerField(blank=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Cap_form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Cap_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.IntegerField(blank=True)),
                ('name', models.CharField(max_length=80)),
                ('colour', models.ForeignKey(to='tables.Colour')),
            ],
        ),
        migrations.CreateModel(
            name='Container_form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Container_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Container_mat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sticker_part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='sticker',
            name='part',
            field=models.ForeignKey(to='tables.Sticker_part'),
        ),
        migrations.AddField(
            model_name='sticker',
            name='product',
            field=models.ForeignKey(to='tables.Product'),
        ),
        migrations.AddField(
            model_name='container',
            name='form',
            field=models.ForeignKey(to='tables.Container_form'),
        ),
        migrations.AddField(
            model_name='container',
            name='group',
            field=models.ForeignKey(to='tables.Container_group'),
        ),
        migrations.AddField(
            model_name='container',
            name='mat',
            field=models.ForeignKey(to='tables.Container_mat'),
        ),
        migrations.AddField(
            model_name='cap',
            name='colour',
            field=models.ForeignKey(to='tables.Colour'),
        ),
        migrations.AddField(
            model_name='cap',
            name='form',
            field=models.ForeignKey(to='tables.Cap_form'),
        ),
        migrations.AddField(
            model_name='cap',
            name='group',
            field=models.ForeignKey(to='tables.Cap_group'),
        ),
        migrations.AddField(
            model_name='cap',
            name='mat',
            field=models.ForeignKey(to='tables.Container_mat'),
        ),
    ]
