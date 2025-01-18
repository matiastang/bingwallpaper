'''
Author: matiastang
Date: 2024-04-09 14:45:10
LastEditors: matiastang
LastEditTime: 2025-01-17 09:59:49
FilePath: /bingwallpaper/gunicorn_config.py
Description: gunicorn配置文件
'''
import multiprocessing

# 并行工作进程数, int，cpu数量*2+1 推荐进程数
workers = multiprocessing.cpu_count() * 2 + 1
# 绑定的ip与端口
bind = "127.0.0.1:8000"
# 工作模式，sync (默认值) eventlet gevent tornado（这个是指定worker为Uvicorn的Worker，为fastapi专属，其他比如flask应用不需要带上这个参数。）
worker_class = "uvicorn.workers.UvicornWorker"
