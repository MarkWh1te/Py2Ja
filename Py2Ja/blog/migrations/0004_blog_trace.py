# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='trace',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6d4f\u89c8\u4eba\u6570'),
        ),
    ]
