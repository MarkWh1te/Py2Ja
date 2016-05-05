# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    title = models.CharField(u"博客标题", max_length=200)
    author = models.CharField(u"博客作者", max_length=200, default="Anonymous")
    brief = models.CharField(u"博客简介", max_length=800, blank=True)
    content = models.TextField(u"博客内容", max_length=20000)
    rank = models.PositiveIntegerField(u"推荐人数", default=0, db_index=True)
    collect = models.PositiveSmallIntegerField(u"关注人数", default=0)
    trace = models.PositiveIntegerField(u"浏览人数", default=0)

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"博客"
        verbose_name_plural = u"博客"


class Commit(models.Model):
    observer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"评论人")
    target = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name=u"评论的博客")
    content = models.CharField(u"评论内容", max_length=1000)
    star = models.PositiveSmallIntegerField(u"好评数", default=0)

    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.observer

    class Meta:
        verbose_name = u"评论"
        verbose_name_plural = u"评论"
