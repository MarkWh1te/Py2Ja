# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0005_codesnippet_trace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesnippet',
            name='rank',
            field=models.PositiveIntegerField(default=0, verbose_name='\u652f\u6301\u4eba\u6570', db_index=True),
        ),
    ]
