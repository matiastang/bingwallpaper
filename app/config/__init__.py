'''
Author: matiastang
Date: 2024-03-12 18:01:49
LastEditors: matiastang
LastEditTime: 2025-01-17 09:52:06
FilePath: /bingwallpaper/app/config/__init__.py
Description: config
'''
import argparse
import os
from functools import lru_cache

from dotenv import load_dotenv

from .app_config import AppConfigSettings


@lru_cache
def getAppConfig() -> AppConfigSettings:
    """ 获取项目配置 """
    # 解析命令行参数
    parseCliArgument()
    # 读取运行环境
    # print("当前运行环境: ", os.environ)
    runEnv = os.environ.get("APP_ENV", "local")
    print("当前运行环境: ", runEnv)
    # 默认加载.env
    envFile = ".env"
    # 运行环境不为空加载 .env 文件
    if runEnv != '' and runEnv != 'local':
        # 当是其他环境时，如测试环境: 加载 .env.test 正式环境: 加载.env.prod
        envFile = runEnv if runEnv.startswith('.env') else f".env.{runEnv}"
    # 加载配置(默认情况下，load_dotenv不回重载已有的环境变量)
    load_dotenv(envFile, override=True)
    # 实例化配置模型
    return AppConfigSettings()


def parseCliArgument():
    """ 解析命令行参数 """
    import sys
    if "uvicorn" in sys.argv[0]:
        # 使用uvicorn启动时，命令行参数只能按照uvicorn的文档来，不能传自定义参数，否则报错
        parser = argparse.ArgumentParser(description="命令行参数")
        parser.add_argument("--env-file", type=str, default="local", help="运行环境")
        # 解析命令行参数
        # args = parser.parse_args()
        # 上面的获取参数的方式，会将gunicorn的启动参数当做输入参数，报如下错误
        # gunicorn: error: unrecognized arguments: -w 4 - k uvicorn.workers.UvicornWorker main: server
        args, unknow = parser.parse_known_args()
        # 设置环境变量
        os.environ["APP_ENV"] = args.env_file
        return
    # 使用 argparse 定义命令行参数
    parser = argparse.ArgumentParser(description="命令行参数")
    parser.add_argument("--env", type=str, default="local", help="运行环境")
    # 解析命令行参数
    # args = parser.parse_args()
    # 上面的获取参数的方式，会将gunicorn的启动参数当做输入参数，报如下错误
    # gunicorn: error: unrecognized arguments: -w 4 - k uvicorn.workers.UvicornWorker main: server
    args, unknow = parser.parse_known_args()
    # 设置环境变量
    os.environ["APP_ENV"] = args.env


# 创建配置实例
appSettings = getAppConfig()
