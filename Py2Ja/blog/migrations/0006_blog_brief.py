# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160408_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='brief',
            field=models.CharField(max_length=800, verbose_name='\u535a\u5ba2\u7b80\u4ecb', blank=True),
        ),
    ]
