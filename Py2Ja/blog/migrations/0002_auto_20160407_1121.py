# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(default=b'Anonymous', max_length=200, verbose_name='\u535a\u5ba2\u4f5c\u8005'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(max_length=20000, verbose_name='\u535a\u5ba2\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name='\u535a\u5ba2\u6807\u9898'),
        ),
    ]
