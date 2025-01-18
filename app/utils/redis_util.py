'''
Author: matiastang
Date: 2024-03-28 18:32:00
LastEditors: matiastang
LastEditTime: 2024-04-23 17:02:25
FilePath: /bingwallpaper/app/utils/redis_util.py
Description: Redis工具函数
'''
import json
from datetime import timedelta

from loguru import logger

from app.config import appSettings
# 使用全局单例更方便
# * 不用通过传递request: Request，再通过request.app.redis来获取app实例了
# * 不用通过延迟导入from main import server来引入定义在main中的app实例了
from app.server.app_server import get_app_server
from app.types.redis_types import RedisValue

REDIS_KEY_PREFIX = appSettings.redis_key_prefix
server = get_app_server()


async def set_cache(key: str, value: RedisValue, ex: timedelta = None) -> bool:
    """缓存到redis

    Args:
        key (str): 缓存key
        value (_type_): 缓存value
        request (Request): 请求
        ex (timedelta, optional): 缓存时间. Defaults to None.

    Returns:
        bool: 是否成功
    """

    if not all((key, value)):
        return False

    params = {
        'name': REDIS_KEY_PREFIX + key,
        'value': value,
    }
    if ex:
        params['ex'] = ex

    if isinstance(value, int | float | str):
        return await server.redis.set(**params)
    else:
        try:
            params['value'] = json.dumps(value)
            return await server.redis.set(**params)
        except json.JSONDecodeError:
            logger.warning(f'缓存Redis失败，key: {key} value: {value}')
            return False


async def get_cache(key: str) -> str:
    """获取redis缓存

    Args:
        key (str): 缓存key
        request (Request): 请求

    Returns:
        str: 缓存值
    """
    return await server.redis.get(REDIS_KEY_PREFIX + key)


async def del_cache(key: str) -> str:
    """删除redis缓存

    Args:
        key (str): 缓存key
        request (Request): 请求

    Returns:
        str: _description_
    """
    return await server.redis.delete(REDIS_KEY_PREFIX + key)
