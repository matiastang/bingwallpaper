'''
Author: matiastang
Date: 2024-04-22 10:19:59
LastEditors: matiastang
LastEditTime: 2025-01-17 12:14:03
FilePath: /bingwallpaper/app/router/wallpaper/api.py
Description: bing壁纸
'''
import json
import random

import requests
from fastapi import APIRouter
from loguru import logger
from starlette.responses import RedirectResponse

from app.types.enum_types import TimezoneName
from app.types.response.http_response import HttpResponse, ResponseFail
from app.types.wallpaper_types import BingWallpaperImage
from app.utils import redis_util, time_util

# 缓存key
WALLPAPER_BING_REDIS_KEY = 'last'

# 路由
router = APIRouter(
    prefix="/wallpaper/bing",
    tags=["wallpaper.bing"],
)


async def get_bing_wallpaper(idx: int = 0, num: int = 1):
    """
    获取bingwallpaper的壁纸信息

    Args:
        idx (int, optional): 图片索引. Defaults to 0.
        num (int, optional): 图片数量. Defaults to 1.

    Returns:
        list[BingWallpaperImage]: 图片列表
    """

    # 目标URL
    url = 'https://cn.bing.com/HPImageArchive.aspx'

    # 请求头
    params = {
        'format': 'js',
        'idx': idx,
        'n': num,
    }

    # 发送GET请求
    res = requests.get(url, params=params)

    # 打印响应内容
    data = res.json()
    images = data.get('images', [])
    return [BingWallpaperImage(**image) for image in images]


@router.get('/last')
async def get_bing_wallpaper_last() -> HttpResponse:
    """ 获取bing的最新一张壁纸 """

    info = await redis_util.get_cache(WALLPAPER_BING_REDIS_KEY)
    if info:
        try:
            images = json.loads(info)
            if isinstance(images, list) and len(images) > 0:
                wallpapers = [BingWallpaperImage(**image) for image in images]
                first_wallpapers = wallpapers[0]
                wallpaper_url = first_wallpapers.url
                url = f"https://cn.bing.com{wallpaper_url}"
                return RedirectResponse(url=url, status_code=302)
        except Exception as e:
            logger.error('-' * 10 + '[LAST]解析缓存壁纸信息失败' + '-' * 10)
            logger.error(e)

    wallpapers = await get_bing_wallpaper()
    if len(wallpapers) > 0:
        try:
            json_str = json.dumps([wallpaper.model_dump() for wallpaper in wallpapers])
            ex = time_util.get_remaining_seconds_in_day(TimezoneName.SHANGHAI)
            status = await redis_util.set_cache(WALLPAPER_BING_REDIS_KEY, json_str, ex)
            if not status:
                logger.error('-' * 10 + '[LAST]壁纸缓存失败' + '-' * 10)
            first_wallpapers = wallpapers[0]
            wallpaper_url = first_wallpapers.url
            url = f"https://cn.bing.com{wallpaper_url}"
            return RedirectResponse(url=url, status_code=302)
        except Exception as e:
            logger.error('-' * 10 + '[LAST]处理壁纸结果失败' + '-' * 10)
            logger.error(e)
    return ResponseFail('获取壁纸失败', 500)


@router.get('/random/{n}')
async def get_bing_wallpaper_random(n: int) -> HttpResponse:
    """ 随机获取最近n张壁纸中的一张 """

    if n <= 0:
        return ResponseFail('参数n必须大于0', 400)

    if n > 8:
        return ResponseFail('参数n不能超过8', 400)

    cache_key = f'random_{n}'
    info = await redis_util.get_cache(cache_key)

    if info:
        try:
            images = json.loads(info)
            if isinstance(images, list) and len(images) > 0:
                wallpapers = [BingWallpaperImage(**image) for image in images]
                selected_wallpaper = random.choice(wallpapers)
                wallpaper_url = selected_wallpaper.url
                url = f"https://cn.bing.com{wallpaper_url}"
                return RedirectResponse(url=url, status_code=302)
        except Exception as e:
            logger.error('-' * 10 + f'[RANDOM_{n}]解析缓存壁纸信息失败' + '-' * 10)
            logger.error(e)

    wallpapers = await get_bing_wallpaper(idx=0, num=n)
    if len(wallpapers) > 0:
        try:
            json_str = json.dumps([wallpaper.model_dump() for wallpaper in wallpapers])
            ex = time_util.get_remaining_seconds_in_day(TimezoneName.SHANGHAI)
            status = await redis_util.set_cache(cache_key, json_str, ex)
            if not status:
                logger.error('-' * 10 + f'[RANDOM_{n}]壁纸缓存失败' + '-' * 10)

            selected_wallpaper = random.choice(wallpapers)
            wallpaper_url = selected_wallpaper.url
            url = f"https://cn.bing.com{wallpaper_url}"
            return RedirectResponse(url=url, status_code=302)
        except Exception as e:
            logger.error('-' * 10 + f'[RANDOM_{n}]处理壁纸结果失败' + '-' * 10)
            logger.error(e)

    return ResponseFail('获取壁纸失败', 500)
