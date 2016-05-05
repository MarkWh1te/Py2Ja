# -*- coding: utf-8 -*-
"""
WSGI config for Py2Ja project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 修改配置文件路径
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Py2Ja.settings.development_settings")

application = get_wsgi_application()
