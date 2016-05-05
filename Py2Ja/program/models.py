# -*- coding: utf-8 -*-
from django.db import models


class CodeSnippet(models.Model):
    CODE_TYPE_CHOICES = (
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('PHP', 'PHP'),
        ('JavaScript', 'JavaScript'),
        ('SQL', 'SQL'),
    )

    snippet = models.TextField(u"代码片段", max_length=10000)
    type = models.CharField(u"代码类型", max_length=50, choices=CODE_TYPE_CHOICES, default='Python')
    description = models.CharField(u"功能描述", max_length=1000)
    coder = models.CharField(u"代码作者", max_length=200, default="Anonymous")
    rank = models.PositiveIntegerField(u"支持人数", default=0, db_index=True)
    collect = models.PositiveSmallIntegerField(u"关注人数", default=0)
    trace = models.PositiveIntegerField(u"浏览人数", default=0)

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.type

    class Meta:
        verbose_name = u"代码片段"
        verbose_name_plural = u"代码片段"
