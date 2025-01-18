'''
Author: matiastang
Date: 2024-03-29 14:53:01
LastEditors: matiastang
LastEditTime: 2024-04-23 16:51:32
FilePath: /bingwallpaper/app/server/app_server.py
Description: FastAPI单例
'''
from contextlib import asynccontextmanager

from loguru import logger
from redis import asyncio

from app.config import appSettings

from .app_fastapi import AppFastAPI

APP_NAME = appSettings.app_name
REDIS_URL = appSettings.redis_url


@asynccontextmanager
async def lifespan(app: AppFastAPI):
    # 日志
    logger.add("logs/log_{time:YYYY-MM-DD}.log", rotation="00:00", retention="7 days", level="INFO")
    # redis
    redis_session = await asyncio.from_url(REDIS_URL, decode_responses=True, encoding="utf8")
    app.redis = redis_session
    logger.info(f'Redis 挂载（{REDIS_URL}）：{"成功" if redis_session else "失败"}')
    yield
    # 相关清除逻辑
    await redis_session.close()
    logger.info('Redis close')


class AppSingleton:
    _instance = None

    @staticmethod
    def get_instance() -> AppFastAPI:
        if not AppSingleton._instance:
            AppSingleton._instance = AppFastAPI(redoc_url=None, title=APP_NAME, lifespan=lifespan)
        return AppSingleton._instance


def get_app_server() -> AppFastAPI:
    return AppSingleton.get_instance()
