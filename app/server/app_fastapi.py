'''
Author: matiastang
Date: 2024-03-29 15:13:20
LastEditors: matiastang
LastEditTime: 2024-04-23 17:15:50
FilePath: /bingwallpaper/app/server/app_fastapi.py
Description: 扩展FastAPI
'''
from typing import Optional

from fastapi import FastAPI
from redis import Redis


class AppFastAPI(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # 挂载的Redis
    redis: Optional[Redis] = None
