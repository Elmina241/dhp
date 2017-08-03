# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0045_auto_20170803_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='boxingAmount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='production',
            name='boxingUnit',
            field=models.ForeignKey(null=True, related_name='boxing_unit', to='tables.Unit'),
        ),
        migrations.AddField(
            model_name='production',
            name='capAmount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='production',
            name='capUnit',
            field=models.ForeignKey(null=True, related_name='cap_unit', to='tables.Unit'),
        ),
        migrations.AddField(
            model_name='production',
            name='contAmount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='production',
            name='contUnit',
            field=models.ForeignKey(null=True, related_name='cont_unit', to='tables.Unit'),
        ),
        migrations.AddField(
            model_name='production',
            name='stickerAmount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='production',
            name='stickerUnit',
            field=models.ForeignKey(null=True, related_name='sticker_unit', to='tables.Unit'),
        ),
    ]
