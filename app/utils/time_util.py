#!/Users/matias/matias/MT/MTGithub/bingwallpaper/venv/bin/python3
# coding=utf-8
'''
Author: matiastang
Date: 2025-01-17 11:26:02
LastEditors: matiastang
LastEditTime: 2025-01-17 12:55:38
FilePath: /bingwallpaper/app/utils/time_util.py
Description: 时间
'''
from datetime import datetime

import pytz

from app.types.enum_types import TimezoneName


def get_remaining_seconds_in_day(timezone_name: TimezoneName = TimezoneName.UTC) -> int:
    """
    获取指定时区当天剩余的时间（秒数）

    Args:
        timezone_name (str): 时区名称（如 "Asia/Shanghai", "UTC"）

    Raises:
        ValueError: 未知时区

    Returns:
        int: 当天剩余时间的秒数
    """
    try:
        # 获取指定时区
        timezone = pytz.timezone(timezone_name.value)

        # 当前时区时间
        # now = datetime.now(timezone)
        now = datetime.now()

        # 当天结束时间（午夜）
        # end_of_day = datetime(now.year, now.month, now.day, 23, 59, 59, tzinfo=timezone)
        end_of_day = datetime(now.year, now.month, now.day, 23, 59, 59)

        end_of_day_test = datetime(now.year, now.month, now.day, 23, 59, 59, tzinfo=timezone)

        # 转换时间
        now_time_tz = timezone.localize(now)
        end_of_day_time_tz = timezone.localize(end_of_day)

        print(end_of_day, end_of_day_test, end_of_day_time_tz)

        # 计算剩余时间
        print(end_of_day, now)
        print(end_of_day_time_tz, now_time_tz)
        # remaining_time = end_of_day - now
        remaining_time = end_of_day_time_tz - now_time_tz
        return int(remaining_time.total_seconds())
    except pytz.UnknownTimeZoneError:
        raise ValueError(f"未知时区: {timezone_name}")


if __name__ == "__main__":
    """
    测试
    python3 -m app.utils.time_util
    """
    print(get_remaining_seconds_in_day(TimezoneName.SHANGHAI))
