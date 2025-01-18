'''
Author: matiastang
Date: 2024-03-13 16:12:14
LastEditors: matiastang
LastEditTime: 2025-01-17 10:01:47
FilePath: /bingwallpaper/app/config/app_config.py
Description: app_config
'''
from pydantic_settings import BaseSettings


class AppConfigSettings(BaseSettings):
    # -------- 应用配置 --------
    app_version: str = ""
    app_env: str = ""
    app_name: str = ""
    app_host: str = ""
    app_port: int = 8000
    app_debug: bool = False

    # -------- Redis配置 --------
    redis_url: str = ""
    redis_key_prefix: str = ""
