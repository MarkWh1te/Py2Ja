# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentIP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField(verbose_name='\u767b\u9646IP', db_index=True)),
            ],
            options={
                'verbose_name': '\u5ba2\u670d\u7aef\u767b\u9646IP',
                'verbose_name_plural': '\u5ba2\u670d\u7aef\u767b\u9646IP',
            },
        ),
    ]
