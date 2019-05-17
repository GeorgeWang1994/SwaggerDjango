#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    george wang
@datetime:  2019-05-18
@file:      serializers.py
@contact:   georgewang1994@163.com
@desc:      序列化
"""

from rest_framework import serializers

from account.manager import get_api_permission_qs_db
from account.models import APIPermission


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    permission_qs = get_api_permission_qs_db()
    snippets = serializers.HyperlinkedRelatedField(queryset=permission_qs, view_name='all_permission', many=True)

    class Meta:
        model = APIPermission
        fields = ('url', 'method', 'role')

