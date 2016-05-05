# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agentip',
            name='ip',
            field=models.GenericIPAddressField(verbose_name='\u767b\u9646IP', db_index=True),
        ),
    ]
