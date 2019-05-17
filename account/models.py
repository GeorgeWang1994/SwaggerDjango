#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:    george wang
@datetime:  2019-05-17
@file:      models.py
@contact:   georgewang1994@163.com
@desc:      表
"""

from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models


class ApiMethod(Enum):
    """
    api方法
    """
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'
    PUT = 'PUT'

    @classmethod
    def get_all_values(cls):
        return [(key, value.value) for key, value in ApiMethod.__members__.items()]


class PermissionRole(Enum):
    """
    权限角色
    """
    SUPER = 'SUPER'
    ADMIN = 'ADMIN'
    USER = 'USER'

    @classmethod
    def get_all_values(cls):
        return [(key, value.value) for key, value in PermissionRole.__members__.items()]


class APIUser(AbstractUser):
    """
    用户信息
    """
    role = models.CharField(max_length=10, choices=PermissionRole.get_all_values(),
                            default=PermissionRole.ADMIN.value, verbose_name="用户角色")

    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")


"""
背景：存在固定的API，需要对API进行权限的验证，每个API有不同的请求方法，也可能有不同的权限；
     并且还有可能会更改API地址（需要做到方便更改），以及能够方便的更改API的权限地址；
     
做法：
    1. 记录一张用户角色对应API和方法的映射表，通过用户角色和API和方法是否能拿到数据来表明是否有权限；
       缺点：如果更改API，需要提供批量修改API的方法；优点：记录冗余信息，提高服务器的性能；
    2. 单独记录API一张表，以及用户角色和API的id和方法的映射；
       缺点：如果需要先根据API从API表拿id，才能进行下一步的判断；优点：如果更改API，可以很方便，不需要提供脚本来刷API；
 
综上，我觉得由于更改API这种做法比较少见，一般发布以后就不会更改API，顶多更改URL参数，而且后台查询是比较频繁的操作，提高查询的性能是必要的；
因此选择第一种方式比较好；       
"""


class APIPermission(models.Model):
    """
    api权限
    """
    role = models.CharField(max_length=10, choices=PermissionRole.get_all_values(),
                            default=PermissionRole.USER.value, verbose_name=u"权限的角色")
    method = models.CharField(max_length=10, choices=ApiMethod.get_all_values(),
                              default=ApiMethod.GET.value, verbose_name=u"API的方法")
    url = models.CharField(max_length=100, verbose_name=u"API的url")

    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        unique_together = ("url", "role", "method")

    def __repr__(self):
        return "%s:%s:%s" % (self.url[10], self.method, self.role)
