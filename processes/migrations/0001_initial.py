# Generated by Django 2.2.1 on 2019-06-18 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kneading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Characteristic')),
                ('kneading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processes.Kneading')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Kneading_char_number',
            fields=[
                ('kneading_char_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='processes.Kneading_char')),
                ('number', models.FloatField()),
            ],
            bases=('processes.kneading_char',),
        ),
        migrations.CreateModel(
            name='Tank_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.FloatField(default=3)),
                ('amount', models.FloatField()),
                ('reserved', models.FloatField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('batch', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='processes.Batch')),
                ('kneading', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='processes.Kneading')),
                ('tank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Tank')),
            ],
        ),
        migrations.CreateModel(
            name='State_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('kneading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processes.Kneading')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processes.State')),
            ],
        ),
        migrations.CreateModel(
            name='Reactor_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.FloatField(default=3)),
                ('reserved', models.FloatField(default=0)),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('batch', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='processes.Batch')),
                ('kneading', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='processes.Kneading')),
                ('reactor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Reactor')),
            ],
        ),
        migrations.CreateModel(
            name='Pack_process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('finished', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Product')),
                ('reactor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Reactor')),
                ('tank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Tank')),
            ],
        ),
        migrations.CreateModel(
            name='Month_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=10)),
                ('num', models.FloatField()),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Model_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='Model_component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.FloatField()),
                ('min', models.FloatField(blank=True, default=0, null=True)),
                ('max', models.FloatField(blank=True, default=0, null=True)),
                ('formula', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Formula')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processes.Model_list')),
                ('mat', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Loading_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.FloatField()),
                ('formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Formula')),
            ],
        ),
        migrations.CreateModel(
            name='List_component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min', models.FloatField(blank=True, default=None, null=True)),
                ('max', models.FloatField(blank=True, default=None, null=True)),
                ('ammount', models.FloatField()),
                ('loaded', models.BooleanField(default=False)),
                ('compl', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Compl_comp')),
                ('formula', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Formula')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processes.Loading_list')),
                ('mat', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Material')),
                ('r_cont', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='processes.Reactor_content')),
                ('t_cont', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='processes.Tank_content')),
            ],
        ),
        migrations.CreateModel(
            name='Kneading_char_var',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_var', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Set_var')),
                ('kneading_char', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processes.Kneading_char')),
            ],
        ),
        migrations.AddField(
            model_name='kneading',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processes.Loading_list'),
        ),
        migrations.AddField(
            model_name='kneading',
            name='reactor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Reactor'),
        ),
        migrations.CreateModel(
            name='Batch_comp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.FloatField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processes.Batch')),
                ('mat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.Material')),
            ],
        ),
        migrations.AddField(
            model_name='batch',
            name='kneading',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='processes.Kneading'),
        ),
    ]
