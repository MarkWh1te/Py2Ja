# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr', '0005_hacker_commit_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hacker',
            name='commit_code',
            field=models.PositiveIntegerField(default=0, verbose_name='\u4ee3\u7801\u6bb5\u8d21\u732e\u6570', db_index=True),
        ),
    ]
