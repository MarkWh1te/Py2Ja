# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hacker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sex', models.CharField(default='\u7537\u751f', max_length=50, verbose_name='\u6027\u522b', choices=[(b'Male', '\u7537\u751f'), (b'Female', '\u5973\u751f')])),
                ('age', models.PositiveSmallIntegerField(default=20, verbose_name='\u5e74\u9f84')),
                ('head_portrait', models.ImageField(upload_to=b'head_portrait', verbose_name='\u5934\u50cf')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7a0b\u5e8f\u5458',
                'verbose_name_plural': '\u7a0b\u5e8f\u5458',
            },
        ),
    ]
