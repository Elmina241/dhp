# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20190401_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='is_edited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='matrix',
            name='access',
            field=models.CharField(max_length=20, default='0', choices=[('0', 'Открыто всем'), ('1', 'Открыто донору'), ('2', 'Открыто акцептору'), ('3', 'Закрыто'), ('4', 'Выполнение')]),
        ),
        migrations.AlterField(
            model_name='matrix',
            name='cause',
            field=models.CharField(max_length=20, default='0', choices=[('0', 'Перемещение'), ('1', 'Оприходование/Выбытие'), ('2', 'Инвентаризация')]),
        ),
    ]
