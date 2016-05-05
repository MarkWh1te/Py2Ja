# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codesnippet',
            name='name',
        ),
        migrations.AddField(
            model_name='codesnippet',
            name='description',
            field=models.CharField(default=datetime.datetime(2016, 4, 6, 7, 5, 37, 235250, tzinfo=utc), max_length=1000, verbose_name='\u529f\u80fd\u63cf\u8ff0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='codesnippet',
            name='type',
            field=models.CharField(default=b'Python', max_length=50, verbose_name='\u4ee3\u7801\u7c7b\u578b', choices=[(b'C++', b'C++'), (b'Java', b'Java'), (b'Python', b'Python'), (b'PHP', b'PHP'), (b'JavaScript', b'JavaScript'), (b'SQL', b'SQL')]),
        ),
    ]
