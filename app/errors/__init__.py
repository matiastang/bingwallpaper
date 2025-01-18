'''
Author: matiastang
Date: 2024-03-12 16:41:57
LastEditors: matiastang
LastEditTime: 2024-04-23 16:56:01
FilePath: /bingwallpaper/app/errors/__init__.py
Description: errors
'''
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from .app_error import appExceptionHandler
from .http_error import httpExceptionHandler
from .validation_error import validationExceptionHandler


def registerCustomErrorHandle(server: FastAPI):
    """ 统一注册自定义错误处理器 """
    # 注册参数验证错误,并覆盖模式RequestValidationError
    server.add_exception_handler(RequestValidationError, validationExceptionHandler)
    # 注册pydantic类型校验错误(ValidationError)的处理函数
    server.add_exception_handler(ValidationError, validationExceptionHandler)
    # 错误处理StarletteHTTPException
    server.add_exception_handler(StarletteHTTPException, httpExceptionHandler)
    # 自定义全局系统错误
    server.add_exception_handler(Exception, appExceptionHandler)
