# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_codesnippet_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='codesnippet',
            name='coder',
            field=models.CharField(default=b'Anonymous', max_length=200, verbose_name='\u4ee3\u7801\u4f5c\u8005'),
        ),
    ]
