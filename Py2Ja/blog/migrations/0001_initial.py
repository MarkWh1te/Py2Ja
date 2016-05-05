# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('content', models.TextField(max_length=20000, verbose_name='\u5185\u5bb9')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to='usr.Hacker')),
            ],
            options={
                'verbose_name': '\u535a\u5ba2',
                'verbose_name_plural': '\u535a\u5ba2',
            },
        ),
    ]
