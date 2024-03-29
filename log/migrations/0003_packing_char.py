# Generated by Django 2.2.3 on 2019-10-07 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0001_initial'),
        ('log', '0002_packing_divergence_pack_amm_set'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packing_char',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('char', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processes.Kneading_char_number')),
                ('packing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Packing_divergence')),
            ],
        ),
    ]
