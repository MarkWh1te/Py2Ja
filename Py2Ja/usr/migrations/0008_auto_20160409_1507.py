# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr', '0007_auto_20160409_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hacker',
            name='commit_blog',
            field=models.PositiveIntegerField(default=0, verbose_name='\u535a\u5ba2\u6587\u7ae0\u8d21\u732e\u6570', db_index=True),
        ),
    ]
