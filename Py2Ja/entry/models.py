# -*- coding: utf-8 -*-
from django.db import models


class AgentIP(models.Model):
    ip = models.GenericIPAddressField (u"登陆IP", db_index=True)

    def __unicode__(self):
        return self.ip

    class Meta:
        verbose_name = u"客服端登陆IP"
        verbose_name_plural = u"客服端登陆IP"
