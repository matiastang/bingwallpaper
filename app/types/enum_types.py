'''
Author: matiastang
Date: 2025-01-17 12:09:15
LastEditors: matiastang
LastEditTime: 2025-01-17 12:11:24
FilePath: /bingwallpaper/app/types/enum_types.py
Description: 枚举
'''
from enum import Enum


class TimezoneName(Enum):
    """时区名称"""

    UTC = 'UTC'

    SHANGHAI = 'Asia/Shanghai'
    """上海"""
