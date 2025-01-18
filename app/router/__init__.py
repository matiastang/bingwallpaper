'''
Author: matiastang
Date: 2024-03-12 18:17:54
LastEditors: matiastang
LastEditTime: 2025-01-17 10:38:07
FilePath: /bingwallpaper/app/router/__init__.py
Description: router
'''
from .wallpaper import api as wallpaper_api

# 定义路由列表
RegisterRouterList = [
    wallpaper_api,
]
