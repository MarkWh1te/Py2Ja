# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160411_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='collect',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u5173\u6ce8\u4eba\u6570'),
        ),
        migrations.AlterField(
            model_name='commit',
            name='star',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u597d\u8bc4\u6570'),
        ),
    ]
