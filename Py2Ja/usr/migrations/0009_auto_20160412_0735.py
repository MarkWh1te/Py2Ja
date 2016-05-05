# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0006_auto_20160408_0558'),
        ('blog', '0008_auto_20160411_1739'),
        ('usr', '0008_auto_20160409_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='hacker',
            name='collect_blogs',
            field=models.ManyToManyField(to='blog.Blog', verbose_name='\u6536\u85cf\u7684\u6587\u7ae0'),
        ),
        migrations.AddField(
            model_name='hacker',
            name='collect_codesnippts',
            field=models.ManyToManyField(to='program.CodeSnippet', verbose_name='\u6536\u85cf\u7684\u4ee3\u7801'),
        ),
        migrations.AlterField(
            model_name='hacker',
            name='hacker',
            field=models.ForeignKey(verbose_name='\u7a0b\u5e8f\u5458', to=settings.AUTH_USER_MODEL),
        ),
    ]
