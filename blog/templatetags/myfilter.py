#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import template

register = template.Library()

# 转换月份的 过滤器

@register.filter()
def month_to_upper(key):
    return ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二'][key.month-1]


# 注册过滤器
# register.filter('month_to_upper', month_to_upper)