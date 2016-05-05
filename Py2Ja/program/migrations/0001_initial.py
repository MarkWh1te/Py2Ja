# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeSnippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('snippet', models.TextField(max_length=10000, verbose_name='\u4ee3\u7801\u7247\u6bb5')),
                ('type', models.CharField(max_length=100, verbose_name='\u4ee3\u7801\u7c7b\u578b')),
                ('name', models.CharField(max_length=200, verbose_name='\u4fdd\u5b58\u540d\u79f0')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u4ee3\u7801\u7247\u6bb5',
                'verbose_name_plural': '\u4ee3\u7801\u7247\u6bb5',
            },
        ),
    ]
