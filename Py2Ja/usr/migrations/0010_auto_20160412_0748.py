# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usr', '0009_auto_20160412_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hacker',
            name='collect_blogs',
            field=models.ManyToManyField(to='blog.Blog', verbose_name='\u6536\u85cf\u7684\u6587\u7ae0', blank=True),
        ),
        migrations.AlterField(
            model_name='hacker',
            name='collect_codesnippts',
            field=models.ManyToManyField(to='program.CodeSnippet', verbose_name='\u6536\u85cf\u7684\u4ee3\u7801', blank=True),
        ),
    ]
