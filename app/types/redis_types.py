'''
Author: matiastang
Date: 2024-03-28 18:45:04
LastEditors: matiastang
LastEditTime: 2025-01-17 11:33:42
FilePath: /bingwallpaper/app/types/redis_types.py
Description: Redis相关类型
'''
from datetime import timedelta
from typing import Any, Optional

from pydantic import BaseModel, Field, field_validator

# Redis 值类型
RedisValue = Any


class RedisBase(BaseModel):
    """ Redis参数基础类 """
    key: str = Field(min_length=1)


class RedisSave(RedisBase):
    """ Redis保存参数类 """
    value: RedisValue
    ex: Optional[timedelta] = None

    @field_validator('value')
    def value_must_not_be_empty(cls, v):
        """ value 不能为空 """
        if v is None or (isinstance(v, str) and not v.strip()):
            raise ValueError('Redis value must not be empty')
        return v
