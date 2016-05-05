# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('usr', '0003_auto_20160405_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hacker',
            name='head_portrait',
        ),
        migrations.AddField(
            model_name='hacker',
            name='avatar_name',
            field=models.CharField(default=datetime.datetime(2016, 4, 5, 14, 39, 59, 960374, tzinfo=utc), max_length=128),
            preserve_default=False,
        ),
    ]
