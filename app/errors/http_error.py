'''
Author: matiastang
Date: 2024-03-12 17:43:50
LastEditors: matiastang
LastEditTime: 2024-04-23 18:16:39
FilePath: /bingwallpaper/app/errors/http_error.py
Description: http error
'''
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from loguru import logger
from starlette.exceptions import HTTPException

from app.types.response.http_response import ResponseFail


async def httpExceptionHandler(request, exc: HTTPException) -> JSONResponse:
    """自定义处理HTTPException"""
    print("request:", request)
    print("status_code:", exc.status_code)
    logger.info(request)
    logger.error(exc)
    if exc.status_code == status.HTTP_404_NOT_FOUND:
        # 处理404错误
        return JSONResponse(
            content=jsonable_encoder(ResponseFail("接口路由不存在~")),
            status_code=status.HTTP_200_OK,
        )
    elif exc.status_code == status.HTTP_405_METHOD_NOT_ALLOWED:
        # 处理405错误
        return JSONResponse(
            content=jsonable_encoder(ResponseFail("请求方式错误，请查看文档确认~")),
            status_code=status.HTTP_200_OK,
        )
    else:
        return JSONResponse(
            content=jsonable_encoder(ResponseFail(str(exc))),
            status_code=status.HTTP_200_OK,
        )
