'''
Author: matiastang
Date: 2024-03-12 17:48:57
LastEditors: matiastang
LastEditTime: 2024-04-23 18:16:17
FilePath: /bingwallpaper/app/errors/app_error.py
Description: app error
'''
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from loguru import logger

from app.types.response.http_response import ResponseFail


async def appExceptionHandler(request: Request, exc: Exception):
    """自定义全局系统错误"""
    print('========全局系统错误（需记录日志）========')
    print(exc)
    logger.error(exc)
    return JSONResponse(
        content=jsonable_encoder(ResponseFail("系统运行异常,稍后重试~")),
        status_code=status.HTTP_200_OK,
        # 跨域时需要在这里添加响应头，不然全局报错的时候讲不支持跨域
        headers={
            'Access-Control-Allow-Origin': "*",  # 允许的来源，可以是字符串、字符串列表，或通配符 "*" （预检请求和正式请求在跨域时候都会验证）
            # 是否允许携带凭证（例如，使用 HTTP 认证、Cookie 等）如果要跨域使用cookies，可以添加上此请求响应头，值设为true
            # （设置或者不设置，都不会影响请求发送，只会影响在跨域时候是否要携带cookies，但是如果设置，预检请求和正式请求都需要设置）。
            # 不过不建议跨域使用（项目中用到过，不过不稳定，有些浏览器带不过去），除非必要，因为有很多方案可以代替。
            'Access-Control-Allow-Credentials': "true",
            'Access-Control-Allow-Methods': "*",  # 允许的 HTTP 方法，可以是字符串、字符串列表，或通配符 "*"（只在预检请求验证）
            'Access-Control-Allow-Headers': "*",  # 允许的 HTTP 头信息，可以是字符串、字符串列表，或通配符 "*"（只在预检请求验证）
            # 允许前端访问的额外响应头，可以是字符串、字符串列表。Access-Control-Expose-Headers: 这个头部让前端代码能够访问在响应中返回的某些自定义头部。
            # 默认情况下，浏览器只能访问一些简单的响应头部，如 Cache-Control, Content-Language, Content-Type, Expires, Last-Modified, 和 Pragma。
            'Access-Control-Expose-Headers': "*",
            'Access-Control-Max-Age': "60000",
            # 请求的缓存时间，以秒为单位。
            # Access-Control-Max-Age: 这个可选的头部指定了预检请求的结果可以被缓存多久。这可以减少不必要的重复预检请求。
        }
    )
