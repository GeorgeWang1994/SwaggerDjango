#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    george wang
@datetime:  2019-05-17
@file:      manager.py
@contact:   georgewang1994@163.com
@desc:      管理操作
"""

from account.models import APIPermission


def get_api_permission_db(url, role, method):
    """
    获取权限记录
    :param role:
    :param url:
    :param method:
    :return:
    """
    try:
        return APIPermission.objects.get(url=url, role=role, method=method)
    except APIPermission.DoesNotExist:
        return None


def get_api_permission_qs_db():
    """
    获取权限记录
    :return:
    """
    return APIPermission.objects.all()
