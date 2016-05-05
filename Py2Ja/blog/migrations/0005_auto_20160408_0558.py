# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_trace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='rank',
            field=models.PositiveIntegerField(default=0, verbose_name='\u63a8\u8350\u4eba\u6570', db_index=True),
        ),
    ]
