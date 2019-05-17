#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    george wang
@datetime:  2019-05-17
@file:      urls.py
@contact:   georgewang1994@163.com
@desc:      url
"""

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from account.views import PermissionView

swagger_view = get_swagger_view(title="测试")

router = DefaultRouter()
router.register(r'users', PermissionView)


urlpatterns = [
    url(r'^$', swagger_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
]
