# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Counter_stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Counterparty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('kind', models.CharField(max_length=20, choices=[('0', 'Организация'), ('1', 'Физлицо'), ('2', 'Административная группа')])),
                ('is_provider', models.BooleanField()),
                ('is_consumer', models.BooleanField()),
                ('is_member', models.BooleanField()),
                ('cur_vin', models.IntegerField(blank=True, default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('abbreviation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('release_date', models.DateField(null=True)),
                ('finish_date', models.DateField(null=True)),
                ('is_edited', models.BooleanField(default=False)),
                ('vin', models.IntegerField(blank=True)),
                ('is_demand', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Demand_good',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=500)),
                ('amount', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Good_name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name_type', models.CharField(max_length=20, choices=[('0', 'Наименование'), ('1', 'Артикул'), ('2', 'Штрихкод')])),
                ('area', models.CharField(max_length=20, choices=[('0', 'Локальное'), ('1', 'Транзитное'), ('2', 'Оригинальное')])),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods_property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('applicable', models.BooleanField()),
                ('visible', models.BooleanField()),
                ('editable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Goods_unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('applicable', models.BooleanField()),
                ('isBase', models.BooleanField()),
                ('coeff', models.FloatField()),
                ('product', models.ForeignKey(to='stock.Goods')),
                ('unit', models.ForeignKey(to='tables.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Matrix',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('access', models.CharField(max_length=20, default='0', choices=[('0', 'Открыто всем'), ('1', 'Открыто донору'), ('2', 'Открыто акцептору'), ('3', 'Закрыто'), ('4', 'Выполнение')])),
                ('cause', models.CharField(max_length=20, default='0', choices=[('0', 'Перемещение'), ('1', 'Оприходование/Выбытие'), ('2', 'Инвентаризация')])),
                ('cause_id', models.IntegerField(null=True, default=0)),
                ('name', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('parent', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model_property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('visible', models.BooleanField()),
                ('editable', models.BooleanField()),
                ('isDefault', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Model_unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('isDonor', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=20, default='0', choices=[('0', 'Свободно'), ('1', 'Заполнение'), ('2', 'Завершено')])),
                ('matrix', models.ForeignKey(to='stock.Matrix')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateTimeField(blank=True)),
                ('vin', models.IntegerField(blank=True)),
                ('matrix', models.ForeignKey(to='stock.Matrix')),
            ],
        ),
        migrations.CreateModel(
            name='Product_model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('group', models.ForeignKey(to='stock.Model_group')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('prop_type', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Property_var',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('cur_vin', models.IntegerField(default='0')),
                ('currency', models.ForeignKey(null=True, to='stock.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_good',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.IntegerField(default=0)),
                ('cost', models.FloatField(blank=True, default=0)),
                ('good', models.ForeignKey(to='stock.Goods')),
                ('stock', models.ForeignKey(to='stock.Stock')),
                ('unit', models.ForeignKey(to='tables.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Stock_operation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('operation', models.CharField(max_length=20, default='0', choices=[('0', 'Приход'), ('1', 'Расход'), ('2', 'Коррекция')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField(default=0)),
                ('cost', models.FloatField(blank=True, default=0)),
                ('last_value', models.FloatField(blank=True, default=0)),
                ('good', models.ForeignKey(to='stock.Goods')),
                ('package', models.ForeignKey(to='stock.Package')),
                ('unit', models.ForeignKey(to='tables.Unit')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='User_group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('group', models.ForeignKey(to='stock.Counterparty')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_allowed', models.BooleanField(default=True)),
                ('section', models.ForeignKey(to='stock.Section')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Default_number',
            fields=[
                ('model_property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Model_property')),
                ('number', models.FloatField()),
            ],
            bases=('stock.model_property',),
        ),
        migrations.CreateModel(
            name='Default_text',
            fields=[
                ('model_property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Model_property')),
                ('text', models.CharField(max_length=200)),
            ],
            bases=('stock.model_property',),
        ),
        migrations.CreateModel(
            name='Default_var',
            fields=[
                ('model_property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Model_property')),
            ],
            bases=('stock.model_property',),
        ),
        migrations.CreateModel(
            name='Goods_string',
            fields=[
                ('goods_property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Goods_property')),
                ('text', models.CharField(max_length=500)),
            ],
            bases=('stock.goods_property',),
        ),
        migrations.CreateModel(
            name='Goods_var',
            fields=[
                ('goods_property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Goods_property')),
            ],
            bases=('stock.goods_property',),
        ),
        migrations.CreateModel(
            name='Property_num',
            fields=[
                ('goods_property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Goods_property')),
                ('number', models.FloatField()),
            ],
            bases=('stock.goods_property',),
        ),
        migrations.CreateModel(
            name='Property_range',
            fields=[
                ('property_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='stock.Property')),
                ('inf', models.FloatField()),
                ('sup', models.FloatField()),
            ],
            bases=('stock.property',),
        ),
        migrations.AddField(
            model_name='property_var',
            name='prop',
            field=models.ForeignKey(to='stock.Property'),
        ),
        migrations.AddField(
            model_name='package',
            name='stock',
            field=models.ForeignKey(to='stock.Stock'),
        ),
        migrations.AddField(
            model_name='order',
            name='stock',
            field=models.ForeignKey(to='stock.Stock'),
        ),
        migrations.AddField(
            model_name='model_unit',
            name='model',
            field=models.ForeignKey(to='stock.Product_model'),
        ),
        migrations.AddField(
            model_name='model_unit',
            name='unit',
            field=models.ForeignKey(to='tables.Unit'),
        ),
        migrations.AddField(
            model_name='model_property',
            name='model',
            field=models.ForeignKey(to='stock.Product_model'),
        ),
        migrations.AddField(
            model_name='model_property',
            name='prop',
            field=models.ForeignKey(to='stock.Property'),
        ),
        migrations.AddField(
            model_name='goods_property',
            name='product',
            field=models.ForeignKey(to='stock.Goods'),
        ),
        migrations.AddField(
            model_name='goods_property',
            name='property',
            field=models.ForeignKey(to='stock.Property'),
        ),
        migrations.AddField(
            model_name='goods',
            name='model',
            field=models.ForeignKey(to='stock.Product_model'),
        ),
        migrations.AddField(
            model_name='goods',
            name='producer',
            field=models.ForeignKey(null=True, default=None, to='stock.Counterparty'),
        ),
        migrations.AddField(
            model_name='good_name',
            name='product',
            field=models.ForeignKey(to='stock.Goods'),
        ),
        migrations.AddField(
            model_name='demand_good',
            name='good',
            field=models.ForeignKey(to='stock.Goods'),
        ),
        migrations.AddField(
            model_name='demand_good',
            name='matrix',
            field=models.ForeignKey(to='stock.Matrix'),
        ),
        migrations.AddField(
            model_name='demand_good',
            name='unit',
            field=models.ForeignKey(to='tables.Unit'),
        ),
        migrations.AddField(
            model_name='demand',
            name='acceptor',
            field=models.ForeignKey(null=True, related_name='acceptor', to='stock.Stock'),
        ),
        migrations.AddField(
            model_name='demand',
            name='consumer',
            field=models.ForeignKey(null=True, related_name='consumer', to='stock.Counterparty'),
        ),
        migrations.AddField(
            model_name='demand',
            name='donor',
            field=models.ForeignKey(null=True, related_name='donor', to='stock.Stock'),
        ),
        migrations.AddField(
            model_name='demand',
            name='matrix',
            field=models.ForeignKey(to='stock.Matrix'),
        ),
        migrations.AddField(
            model_name='demand',
            name='provider',
            field=models.ForeignKey(null=True, related_name='provider', to='stock.Counterparty'),
        ),
        migrations.AddField(
            model_name='demand',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='counter_stock',
            name='counter',
            field=models.ForeignKey(to='stock.Counterparty'),
        ),
        migrations.AddField(
            model_name='counter_stock',
            name='stock',
            field=models.ForeignKey(to='stock.Stock'),
        ),
        migrations.AddField(
            model_name='goods_var',
            name='var',
            field=models.ForeignKey(to='stock.Property_var'),
        ),
        migrations.AddField(
            model_name='default_var',
            name='var',
            field=models.ForeignKey(to='stock.Property_var'),
        ),
    ]
