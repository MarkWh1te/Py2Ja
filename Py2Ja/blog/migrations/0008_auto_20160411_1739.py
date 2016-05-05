# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_commit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='star',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u70b9\u8d5e\u6570'),
        ),
    ]
