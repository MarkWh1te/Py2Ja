# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_blog_brief'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=1000, verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('star', models.PositiveSmallIntegerField(default=0, verbose_name='\u70b9\u8d5e')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('observer', models.ForeignKey(verbose_name='\u8bc4\u8bba\u4eba', to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(verbose_name='\u8bc4\u8bba\u7684\u535a\u5ba2', to='blog.Blog')),
            ],
            options={
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
    ]
