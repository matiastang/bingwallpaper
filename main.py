#!/Users/matias/matias/MT/MTGithub/bingwallpaper/venv/bin/python3
# coding=utf-8
'''
Author: matiastang
Date: 2024-03-12 15:17:12
LastEditors: matiastang
LastEditTime: 2025-01-16 18:53:06
FilePath: /bingwallpaper/main.py
Description: 启动文件
'''
import multiprocessing
import time

import uvicorn
from loguru import logger

from app import errors, middleware
from app.config import appSettings
from app.router import RegisterRouterList
from app.server.app_server import get_app_server
from app.types.response.http_response import ResponseSuccess

# 创建实例
server = get_app_server()

# 注册中间件
middleware.registerMiddlewareHandle(server)

# 注册自定义错误处理器
errors.registerCustomErrorHandle(server)


@server.get("/test")
def server_test():
    """
    测试接口
    """
    now_time = time.time()
    cpu_count = multiprocessing.cpu_count()
    return ResponseSuccess(f"Hello tdy time: {now_time} cpu count: {cpu_count}")


for item in RegisterRouterList:
    """
    注册路由
    """
    server.include_router(item.router)

if __name__ == "__main__":
    """
    启动服务
    """
    logger.info(appSettings)
    # 启动服务
    uvicorn.run(app='main:server', host=appSettings.app_host, port=appSettings.app_port, reload=True)
