# Generated by Django 2.2.1 on 2021-03-17 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_auto_20210306_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='formula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tables.Formula', verbose_name='Вариант состава'),
        ),
    ]
