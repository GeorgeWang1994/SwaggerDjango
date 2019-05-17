#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    george wang
@datetime:  2019-05-17
@file:      views.py
@contact:   georgewang1994@163.com
@desc:      调用方法
"""
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import viewsets

from account.manager import get_api_permission_db, get_api_permission_qs_db
from account.serializers import PermissionSerializer


@login_required
def get_role_api_permission_view(request):
    """
    获取用户的API的访问权限
    URL[GET]: /account/permission/info/
    :param request: {role, url}
    :return: {"have_permission": bool}
    """
    user = request.user
    url = request.path
    method = request.method

    if not url or not method:
        return HttpResponse(json.dumps({"have_permission": False}), content_type="application/json")

    api_permission = get_api_permission_db(url=url, role=user.role, method=method)
    if not api_permission:
        return HttpResponse(json.dumps({"have_permission": False}), content_type="application/json")

    return HttpResponse(json.dumps({"have_permission": True}), content_type="application/json")


class PermissionView(viewsets.ReadOnlyModelViewSet):
    """
    获取全部的访问权限
    """
    queryset = get_api_permission_qs_db()
    serializer_class = PermissionSerializer
