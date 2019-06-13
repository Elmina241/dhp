# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('finish_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Batch_comp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ammount', models.FloatField()),
                ('batch', models.ForeignKey(to='processes.Batch')),
                ('mat', models.ForeignKey(to='tables.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Kneading',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('batch_num', models.FloatField(default=0)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('isValid', models.BooleanField(default=False)),
                ('isFinished', models.BooleanField(default=False)),
            ],
        ),
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
            name='List_component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('min', models.FloatField(blank=True, null=True, default=None)),
                ('max', models.FloatField(blank=True, null=True, default=None)),
                ('ammount', models.FloatField()),
                ('loaded', models.BooleanField(default=False)),
                ('compl', models.ForeignKey(blank=True, null=True, default=None, to='tables.Compl_comp')),
                ('formula', models.ForeignKey(blank=True, null=True, default=None, to='tables.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='Loading_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ammount', models.FloatField()),
                ('formula', models.ForeignKey(to='tables.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='Model_component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ammount', models.FloatField()),
                ('min', models.FloatField(blank=True, null=True, default=0)),
                ('max', models.FloatField(blank=True, null=True, default=0)),
                ('formula', models.ForeignKey(blank=True, null=True, default=None, to='tables.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='Model_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('formula', models.ForeignKey(to='tables.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='Month_plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('month', models.CharField(max_length=10)),
                ('num', models.FloatField()),
                ('prod', models.ForeignKey(to='tables.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Pack_process',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('finished', models.BooleanField(default=False)),
                ('product', models.ForeignKey(to='tables.Product')),
                ('reactor', models.ForeignKey(null=True, to='tables.Reactor')),
                ('tank', models.ForeignKey(null=True, to='tables.Tank')),
            ],
        ),
        migrations.CreateModel(
            name='Reactor_content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content_type', models.FloatField(default=3)),
                ('reserved', models.FloatField(default=0)),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('batch', models.ForeignKey(blank=True, null=True, default=None, to='processes.Batch')),
                ('kneading', models.ForeignKey(blank=True, null=True, default=None, to='processes.Kneading')),
                ('reactor', models.ForeignKey(to='tables.Reactor')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='State_log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('kneading', models.ForeignKey(to='processes.Kneading')),
                ('state', models.ForeignKey(to='processes.State')),
            ],
        ),
        migrations.CreateModel(
            name='Tank_content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content_type', models.FloatField(default=3)),
                ('amount', models.FloatField()),
                ('reserved', models.FloatField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('batch', models.ForeignKey(blank=True, null=True, default=None, to='processes.Batch')),
                ('kneading', models.ForeignKey(blank=True, null=True, default=None, to='processes.Kneading')),
                ('tank', models.ForeignKey(to='tables.Tank')),
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
            model_name='model_component',
            name='list',
            field=models.ForeignKey(to='processes.Model_list'),
        ),
        migrations.AddField(
            model_name='model_component',
            name='mat',
            field=models.ForeignKey(blank=True, null=True, default=None, to='tables.Material'),
        ),
        migrations.AddField(
            model_name='list_component',
            name='list',
            field=models.ForeignKey(to='processes.Loading_list'),
        ),
        migrations.AddField(
            model_name='list_component',
            name='mat',
            field=models.ForeignKey(blank=True, null=True, default=None, to='tables.Material'),
        ),
        migrations.AddField(
            model_name='list_component',
            name='r_cont',
            field=models.ForeignKey(blank=True, null=True, default=None, to='processes.Reactor_content'),
        ),
        migrations.AddField(
            model_name='list_component',
            name='t_cont',
            field=models.ForeignKey(blank=True, null=True, default=None, to='processes.Tank_content'),
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
        migrations.AddField(
            model_name='kneading',
            name='list',
            field=models.ForeignKey(to='processes.Loading_list'),
        ),
        migrations.AddField(
            model_name='kneading',
            name='reactor',
            field=models.ForeignKey(to='tables.Reactor'),
        ),
        migrations.AddField(
            model_name='batch',
            name='kneading',
            field=models.OneToOneField(to='processes.Kneading'),
        ),
    ]
