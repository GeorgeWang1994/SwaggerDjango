#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    george wang
@datetime:  2019-05-17
@file:      admin.py
@contact:   georgewang1994@163.com
@desc:      表后台
"""

from django.contrib import admin

from account.models import APIUser, APIPermission

admin.site.register(APIUser)
admin.site.register(APIPermission)
