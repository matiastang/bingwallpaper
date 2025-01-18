'''
Author: matiastang
Date: 2024-03-13 14:03:23
LastEditors: matiastang
LastEditTime: 2025-01-17 09:33:07
FilePath: /bingwallpaper/app/middleware/__init__.py
Description: 中间件
'''
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .usetime_middleware import UseTimeMiddleware


def registerMiddlewareHandle(server: FastAPI):
    """
    注册中间件

    Args:
        server (FastAPI): FastAPI 实例
    """
    # 添加耗时请求中间件
    server.add_middleware(UseTimeMiddleware)
    # 跨域中间件
    server.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 允许的来源，可以是字符串、字符串列表，或通配符 "*"
        allow_credentials=True,  # 是否允许携带凭证（例如，使用 HTTP 认证、Cookie 等）
        allow_methods=["*"],  # 允许的 HTTP 方法，可以是字符串、字符串列表，或通配符 "*"
        allow_headers=["*"],  # 允许的 HTTP 头信息，可以是字符串、字符串列表，或通配符 "*"
        expose_headers=["*"],  # 允许前端访问的额外响应头，可以是字符串、字符串列表
        max_age=600,  # 请求的缓存时间，以秒为单位
    )
