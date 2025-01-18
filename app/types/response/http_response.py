'''
Author: matiastang
Date: 2024-03-12 17:05:34
LastEditors: matiastang
LastEditTime: 2025-01-17 09:35:21
FilePath: /bingwallpaper/app/types/response/http_response.py
Description: http response
'''
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class Additional(BaseModel):
    """额外信息"""
    time: str
    timestamp: float


class HttpResponse(BaseModel):
    """http统一响应"""
    code: int = Field(default=200)  # 响应码
    msg: str = Field(default="处理成功")  # 响应信息
    data: Any | None  # 具体数据
    additional: Additional  # 额外信息


def ResponseSuccess(resp: Any, msg: str = '处理成功') -> HttpResponse:
    """成功响应"""
    datetimeNow = datetime.now()
    currentTimestamp = datetimeNow.timestamp()
    currentTime = datetimeNow.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(
        data=resp,
        msg=msg,
        additional=Additional(
            time=currentTime,
            timestamp=currentTimestamp,
        ))


def ResponseFail(msg: str, code: int = 500) -> HttpResponse:
    """响应失败"""
    datetimeNow = datetime.now()
    currentTimestamp = datetimeNow.timestamp()
    currentTime = datetimeNow.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(
        code=code,
        msg=msg,
        data=None,
        additional=Additional(
            time=currentTime,
            timestamp=currentTimestamp,
        ))
