# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Box_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Boxing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('form', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Boxing_mat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Cap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('form', models.CharField(max_length=80)),
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
            name='Char_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
                ('is_general', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic_set_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic_type',
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
            name='Comp_char_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comp_prop_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compl_comp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('ammount', models.FloatField()),
                ('reserved', models.FloatField(default=0)),
                ('store_amount', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Compl_comp_comp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ammount', models.FloatField()),
                ('compl', models.ForeignKey(to='tables.Compl_comp')),
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
                ('code', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('sgr', models.CharField(max_length=80)),
                ('sh_life', models.IntegerField(default=24)),
                ('date', models.DateField(null=True)),
                ('package', models.CharField(max_length=80, null=True)),
                ('standard', models.CharField(max_length=80, null=True)),
                ('certificate', models.CharField(max_length=80, null=True)),
                ('declaration', models.CharField(max_length=80, null=True)),
                ('cur_batch', models.FloatField(default=1)),
                ('isFinal', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Composition_char',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('form', models.CharField(max_length=80)),
                ('colour', models.ForeignKey(to='tables.Colour')),
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
            name='Formula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80, null=True)),
                ('cur_batch', models.FloatField(default=1)),
                ('composition', models.ForeignKey(to='tables.Composition')),
            ],
        ),
        migrations.CreateModel(
            name='Formula_component',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ammount', models.FloatField()),
                ('formula', models.ForeignKey(to='tables.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='Mat_char_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('reserved', models.FloatField(default=0)),
                ('concentration', models.FloatField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Material_char',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('option', models.CharField(max_length=80)),
                ('detail', models.CharField(max_length=80)),
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
            name='Product_use',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('compAmount', models.FloatField(default=0)),
                ('contAmount', models.FloatField(default=0)),
                ('capAmount', models.FloatField(default=0)),
                ('stickerAmount', models.FloatField(default=0)),
                ('boxingAmount', models.FloatField(default=0)),
                ('boxing', models.ForeignKey(to='tables.Boxing')),
            ],
        ),
        migrations.CreateModel(
            name='Reactor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('product', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=80)),
                ('min', models.FloatField()),
                ('max', models.FloatField()),
                ('ready', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Set_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
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
            name='Tank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('code', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('capacity', models.FloatField()),
                ('ready', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic_number',
            fields=[
                ('characteristic_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Characteristic')),
                ('inf', models.FloatField()),
                ('sup', models.FloatField()),
            ],
            bases=('tables.characteristic',),
        ),
        migrations.CreateModel(
            name='Characteristic_range',
            fields=[
                ('characteristic_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Characteristic')),
                ('inf', models.FloatField()),
                ('sup', models.FloatField()),
            ],
            bases=('tables.characteristic',),
        ),
        migrations.CreateModel(
            name='Comp_char_number',
            fields=[
                ('composition_char_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Composition_char')),
                ('number', models.FloatField()),
            ],
            bases=('tables.composition_char',),
        ),
        migrations.CreateModel(
            name='Comp_char_range',
            fields=[
                ('composition_char_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Composition_char')),
                ('inf', models.FloatField()),
                ('sup', models.FloatField()),
            ],
            bases=('tables.composition_char',),
        ),
        migrations.CreateModel(
            name='Comp_prop_number',
            fields=[
                ('composition_char_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Composition_char')),
                ('number', models.FloatField()),
            ],
            bases=('tables.composition_char',),
        ),
        migrations.CreateModel(
            name='Mat_char_number',
            fields=[
                ('material_char_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='tables.Material_char')),
                ('number', models.FloatField()),
            ],
            bases=('tables.material_char',),
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
            model_name='production',
            name='boxingUnit',
            field=models.ForeignKey(null=True, related_name='boxing_unit', to='tables.Unit'),
        ),
        migrations.AddField(
            model_name='production',
            name='cap',
            field=models.ForeignKey(to='tables.Cap'),
        ),
        migrations.AddField(
            model_name='production',
            name='capUnit',
            field=models.ForeignKey(null=True, related_name='cap_unit', to='tables.Unit'),
        ),
        migrations.AddField(
            model_name='production',
            name='compUnit',
            field=models.ForeignKey(null=True, to='tables.Unit'),
        ),
        migrations.AddField(
            model_name='production',
            name='composition',
            field=models.ForeignKey(to='tables.Composition'),
        ),
        migrations.AddField(
            model_name='production',
            name='contUnit',
            field=models.ForeignKey(null=True, related_name='cont_unit', to='tables.Unit'),
        ),
        migrations.AddField(
            model_name='production',
            name='container',
            field=models.ForeignKey(to='tables.Container'),
        ),
        migrations.AddField(
            model_name='production',
            name='sticker',
            field=models.ForeignKey(to='tables.Sticker'),
        ),
        migrations.AddField(
            model_name='production',
            name='stickerUnit',
            field=models.ForeignKey(null=True, related_name='sticker_unit', to='tables.Unit'),
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
            name='production',
            field=models.OneToOneField(null=True, to='tables.Production'),
        ),
        migrations.AddField(
            model_name='product',
            name='use',
            field=models.ForeignKey(to='tables.Product_use'),
        ),
        migrations.AddField(
            model_name='material_char',
            name='characteristic',
            field=models.ForeignKey(to='tables.Characteristic'),
        ),
        migrations.AddField(
            model_name='material_char',
            name='mat',
            field=models.ForeignKey(to='tables.Material'),
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
            model_name='mat_char_var',
            name='char_var',
            field=models.ForeignKey(to='tables.Set_var'),
        ),
        migrations.AddField(
            model_name='mat_char_var',
            name='mat_char',
            field=models.ForeignKey(to='tables.Material_char'),
        ),
        migrations.AddField(
            model_name='formula_component',
            name='mat',
            field=models.ForeignKey(to='tables.Material'),
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
            model_name='composition_char',
            name='characteristic',
            field=models.ForeignKey(to='tables.Characteristic'),
        ),
        migrations.AddField(
            model_name='composition_char',
            name='comp',
            field=models.ForeignKey(to='tables.Composition'),
        ),
        migrations.AddField(
            model_name='composition',
            name='form',
            field=models.ForeignKey(null=True, to='tables.Product_form'),
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
            model_name='compl_comp_comp',
            name='mat',
            field=models.ForeignKey(to='tables.Material'),
        ),
        migrations.AddField(
            model_name='compl_comp',
            name='form',
            field=models.ForeignKey(blank=True, null=True, to='tables.Product_form'),
        ),
        migrations.AddField(
            model_name='compl_comp',
            name='formula',
            field=models.ForeignKey(blank=True, null=True, default=None, to='tables.Formula'),
        ),
        migrations.AddField(
            model_name='comp_prop_var',
            name='char_var',
            field=models.ForeignKey(to='tables.Set_var'),
        ),
        migrations.AddField(
            model_name='comp_prop_var',
            name='comp_prop',
            field=models.ForeignKey(to='tables.Composition_char'),
        ),
        migrations.AddField(
            model_name='comp_char_var',
            name='char_var',
            field=models.ForeignKey(to='tables.Set_var'),
        ),
        migrations.AddField(
            model_name='comp_char_var',
            name='comp_char',
            field=models.ForeignKey(to='tables.Composition_char'),
        ),
        migrations.AddField(
            model_name='characteristic_set_var',
            name='char_set',
            field=models.ForeignKey(to='tables.Characteristic'),
        ),
        migrations.AddField(
            model_name='characteristic_set_var',
            name='char_var',
            field=models.ForeignKey(to='tables.Set_var'),
        ),
        migrations.AddField(
            model_name='characteristic',
            name='char_type',
            field=models.ForeignKey(default=1, to='tables.Characteristic_type'),
        ),
        migrations.AddField(
            model_name='characteristic',
            name='group',
            field=models.ForeignKey(to='tables.Char_group'),
        ),
        migrations.AddField(
            model_name='cap',
            name='colour',
            field=models.ForeignKey(to='tables.Colour'),
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
        migrations.AddField(
            model_name='boxing',
            name='colour',
            field=models.ForeignKey(null=True, to='tables.Colour'),
        ),
        migrations.AddField(
            model_name='boxing',
            name='group',
            field=models.ForeignKey(null=True, to='tables.Box_group'),
        ),
        migrations.AddField(
            model_name='boxing',
            name='mat',
            field=models.ForeignKey(null=True, to='tables.Boxing_mat'),
        ),
    ]
