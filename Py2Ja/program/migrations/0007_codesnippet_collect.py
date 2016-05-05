# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0006_auto_20160408_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='codesnippet',
            name='collect',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u5173\u6ce8\u4eba\u6570'),
        ),
    ]
