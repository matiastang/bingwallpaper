'''
Author: matiastang
Date: 2025-01-17 10:19:54
LastEditors: matiastang
LastEditTime: 2025-01-17 12:09:26
FilePath: /bingwallpaper/app/types/wallpaper_types.py
Description: wallpaper types
'''
from typing import Any, List

# from fastapi import File
from pydantic import BaseModel, field_validator


class BingWallpaperImage(BaseModel):
    """
    Bing壁纸图片类型
    """
    startdate: str
    fullstartdate: str
    enddate: str
    url: str
    urlbase: str
    copyright: str
    copyrightlink: str
    title: str
    quiz: str
    wp: bool
    hsh: str
    drk: int
    top: int
    bot: int
    hs: List[Any]

    @field_validator('url')
    def uri_format(cls, v: str):
        """ url必须以/开头 """
        if not v.startswith("/"):
            raise ValueError('url必须以/开头')
        return v
