# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boxing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Cap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
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
            name='Components',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('min', models.FloatField()),
                ('max', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=80)),
                ('sgr', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Composition_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
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
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('mark', models.CharField(max_length=80)),
                ('ammount', models.FloatField()),
                ('concentration', models.FloatField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Material_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=13)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Product_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product_form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product_mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product_option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product_use',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Sticker_part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
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
            model_name='product',
            name='detail',
            field=models.ForeignKey(to='tables.Product_detail'),
        ),
        migrations.AddField(
            model_name='product',
            name='form',
            field=models.ForeignKey(to='tables.Product_form'),
        ),
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.ForeignKey(to='tables.Product_group'),
        ),
        migrations.AddField(
            model_name='product',
            name='mark',
            field=models.ForeignKey(to='tables.Product_mark'),
        ),
        migrations.AddField(
            model_name='product',
            name='option',
            field=models.ForeignKey(to='tables.Product_option'),
        ),
        migrations.AddField(
            model_name='product',
            name='use',
            field=models.ForeignKey(to='tables.Product_use'),
        ),
        migrations.AddField(
            model_name='material',
            name='group',
            field=models.ForeignKey(to='tables.Material_group'),
        ),
        migrations.AddField(
            model_name='material',
            name='prefix',
            field=models.ForeignKey(to='tables.Prefix'),
        ),
        migrations.AddField(
            model_name='material',
            name='unit',
            field=models.ForeignKey(to='tables.Unit'),
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
            model_name='composition',
            name='group',
            field=models.ForeignKey(to='tables.Composition_group'),
        ),
        migrations.AddField(
            model_name='components',
            name='comp',
            field=models.ForeignKey(to='tables.Composition'),
        ),
        migrations.AddField(
            model_name='components',
            name='mat',
            field=models.ForeignKey(to='tables.Material'),
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
