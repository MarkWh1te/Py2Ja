# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr', '0002_auto_20160405_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hacker',
            name='head_portrait',
            field=models.ImageField(upload_to=b'head_portrait', verbose_name='\u5934\u50cf', blank=True),
        ),
    ]
