# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from upload_avatar.models import UploadAvatarMixIn
from upload_avatar.signals import avatar_crop_done

from blog.models import Blog
from program.models import CodeSnippet


class Hacker(models.Model, UploadAvatarMixIn):
    hacker = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, verbose_name=u"程序员")
    sex = models.CharField(u"性别", choices=(("Male", u"男生"), ("Female", u"女生")),
                           default=u"男生", max_length=50)
    age = models.PositiveSmallIntegerField(u"年龄", default=20)
    avatar_name = models.CharField(max_length=128)
    commit_code = models.PositiveIntegerField(u"代码片段贡献数", default=0, db_index=True)
    commit_blog = models.PositiveIntegerField(u"博客文章贡献数", default=0, db_index=True)
    collect_blogs = models.ManyToManyField(Blog, verbose_name=u"收藏的文章", blank=True, related_name="collect_blogs")
    collect_codesnippts = models.ManyToManyField(CodeSnippet, verbose_name=u"收藏的代码",
                                                 blank=True, related_name="collect_codesnippts")

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def get_uid(self):
        return self.hacker.id

    def get_avatar_name(self, size):
        return UploadAvatarMixIn.build_avatar_name(self, self.avatar_name, size)

    def __unicode__(self):
        return self.hacker.username

    class Meta:
        verbose_name = u"程序员"
        verbose_name_plural = u"程序员"


def save_avatar_in_db(sender, uid, avatar_name, **kwargs):
    if Hacker.objects.filter(user_id=uid).exists():
        Hacker.objects.filter(user_id=uid).update(avatar_name=avatar_name)
    else:
        Hacker.objects.create(user_id=uid, avatar_name=avatar_name)

avatar_crop_done.connect(save_avatar_in_db)
