# Generated by Django 2.2.1 on 2019-06-27 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_order_cause'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand_good',
            name='article',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
