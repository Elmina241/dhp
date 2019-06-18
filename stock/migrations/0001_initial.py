# Generated by Django 2.2.1 on 2019-06-18 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tables', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Counterparty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kind', models.CharField(choices=[('0', 'Организация'), ('1', 'Физлицо'), ('2', 'Административная группа')], max_length=20)),
                ('is_provider', models.BooleanField()),
                ('is_consumer', models.BooleanField()),
                ('is_member', models.BooleanField()),
                ('cur_vin', models.IntegerField(blank=True, default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('abbreviation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Goods_property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicable', models.BooleanField()),
                ('visible', models.BooleanField()),
                ('editable', models.BooleanField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Matrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access', models.CharField(choices=[('0', 'Открыто всем'), ('1', 'Открыто донору'), ('2', 'Открыто акцептору'), ('3', 'Закрыто'), ('4', 'Выполнение')], default='0', max_length=20)),
                ('cause', models.CharField(choices=[('0', 'Перемещение'), ('1', 'Оприходование/Выбытие'), ('2', 'Инвентаризация')], default='0', max_length=20)),
                ('cause_id', models.IntegerField(default=0, null=True)),
                ('name', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('parent', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model_property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField()),
                ('editable', models.BooleanField()),
                ('isDefault', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True)),
                ('vin', models.IntegerField(blank=True)),
                ('matrix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Matrix')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('prop_type', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cur_vin', models.IntegerField(default='0')),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Default_number',
            fields=[
                ('model_property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Model_property')),
                ('number', models.FloatField()),
            ],
            bases=('stock.model_property',),
        ),
        migrations.CreateModel(
            name='Default_text',
            fields=[
                ('model_property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Model_property')),
                ('text', models.CharField(max_length=200)),
            ],
            bases=('stock.model_property',),
        ),
        migrations.CreateModel(
            name='Goods_string',
            fields=[
                ('goods_property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Goods_property')),
                ('text', models.CharField(max_length=500)),
            ],
            bases=('stock.goods_property',),
        ),
        migrations.CreateModel(
            name='Property_num',
            fields=[
                ('goods_property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Goods_property')),
                ('number', models.FloatField()),
            ],
            bases=('stock.goods_property',),
        ),
        migrations.CreateModel(
            name='Property_range',
            fields=[
                ('property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Property')),
                ('inf', models.FloatField()),
                ('sup', models.FloatField()),
            ],
            bases=('stock.property',),
        ),
        migrations.CreateModel(
            name='User_permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_allowed', models.BooleanField(default=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Section')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Counterparty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stock_operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(choices=[('0', 'Приход'), ('1', 'Расход'), ('2', 'Коррекция')], default='0', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField(default=0)),
                ('cost', models.FloatField(blank=True, default=0)),
                ('last_value', models.FloatField(blank=True, default=0)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Goods')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Package')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Unit')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Stock_good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('cost', models.FloatField(blank=True, default=0)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Goods')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Property_var',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Property')),
            ],
        ),
        migrations.CreateModel(
            name='Product_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Model_group')),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDonor', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('0', 'Свободно'), ('1', 'Заполнение'), ('2', 'Завершено')], default='0', max_length=20)),
                ('matrix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Matrix')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='Model_unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Product_model')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Unit')),
            ],
        ),
        migrations.AddField(
            model_name='model_property',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Product_model'),
        ),
        migrations.AddField(
            model_name='model_property',
            name='prop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Property'),
        ),
        migrations.CreateModel(
            name='Goods_unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicable', models.BooleanField()),
                ('isBase', models.BooleanField()),
                ('coeff', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Goods')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Unit')),
            ],
        ),
        migrations.AddField(
            model_name='goods_property',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Property'),
        ),
        migrations.AddField(
            model_name='goods',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Product_model'),
        ),
        migrations.AddField(
            model_name='goods',
            name='producer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.Counterparty'),
        ),
        migrations.CreateModel(
            name='Good_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_type', models.CharField(choices=[('0', 'Наименование'), ('1', 'Артикул'), ('2', 'Штрихкод')], max_length=20)),
                ('area', models.CharField(choices=[('0', 'Локальное'), ('1', 'Транзитное'), ('2', 'Оригинальное')], max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Demand_good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('amount', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Goods')),
                ('matrix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Matrix')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('release_date', models.DateField(null=True)),
                ('finish_date', models.DateField(null=True)),
                ('is_edited', models.BooleanField(default=False)),
                ('vin', models.IntegerField(blank=True)),
                ('is_demand', models.BooleanField(default=True)),
                ('acceptor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acceptor', to='stock.Stock')),
                ('consumer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='consumer', to='stock.Counterparty')),
                ('donor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donor', to='stock.Stock')),
                ('matrix', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Matrix')),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider', to='stock.Counterparty')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Counter_stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Counterparty')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='Goods_var',
            fields=[
                ('goods_property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Goods_property')),
                ('var', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Property_var')),
            ],
            bases=('stock.goods_property',),
        ),
        migrations.CreateModel(
            name='Default_var',
            fields=[
                ('model_property_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Model_property')),
                ('var', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Property_var')),
            ],
            bases=('stock.model_property',),
        ),
    ]
