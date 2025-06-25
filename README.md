<!--
 * @Author: matiastang
 * @Date: 2025-01-16 18:13:19
 * @LastEditors: matiastang
 * @LastEditTime: 2025-06-25 16:04:09
 * @FilePath: /bingwallpaper/README.md
 * @Description: README
-->
# bingwallpaper

用`FastAPI`实现一个接口，使用自定义策略重定向到`Bing Wallpaper`的壁纸图片地址。可以用来追随`Bing Wallpaper`的壁纸更新。

部署后的效果，如：[获取今日微软bing壁纸](https://api.tdytech.cn/api/wallpaper/bing/last)

## 环境

我们需要使用`Python`自带的`venv`创建虚拟环境，所以希望使用`python3.11+`的版本，当前这个项目比较简单，对版本没有太高的要求。
```sh
$ python3 --version
Python 3.11.9
```

## 虚拟环境

### 使用`venv`创建虚拟环境

创建虚拟环境
```sh
$ python3 -m venv venv
```

进入虚拟环境
```sh
$ source venv/bin/activate
(venv) root@iZ7xvfrafhk3mj9ma5nn6lZ:~#
```

退出虚拟环境
```sh
$ deactivate
```

## 安装依赖

安装`requirements.txt`依赖
```sh
$ pip3 install -r requirements.txt
```

生成依赖
```sh
$ pip3 freeze > requirements.txt
```
这里建议使用脚本并结合`git hooks`自动生成依赖。具体方法可以参考：[`Pythone项目如何优雅的生成依赖文件`](https://matiastang.github.io/article/yukb34ys.html)

**注意** 建议创建虚拟环境导入依赖

## 依赖说明

* 引入`fastapi`
* 引入`uvicorn`，用于启动`ASGI`服务
`ASGI` 服务器，生产环境可以使用 ['Uvicorn[*]'](https://www.uvicorn.org) 或者 ['Hypercorn[*]'](https://gitlab.com/pgjones/hypercorn)。
* 引入`pydantic`校验参数
* 引入`pydantic_settings`定义配置参数
* 引入`loguru`日志记录
* 引入`redis`数据库
* 引入`isort`整理头文件
* 引入`flake8`、`hacking`、`flake8-chart`格式校验
* 引入`autopep8`自动修复
* 引入`pre-commit`实现`git hooks`的提交审核
* 引入`gunicorn`优化请求并发性能
* 引入`requests`支持请求

**注意** 这个需求比较小，这里的`redis`未使用链接池。
**注意** 部署时有些库不是必须`install`的，可以省略，如`gunicorn`。`gunicorn`只是用来多进程启动的，如果不需要则可以忽略，需要时再添加也可以。

## 启动

项目有三种启动方式：

* 直接使用`python`命令启动
* 通过`uvicorn`启动
* 使用`gunicorn`启动
* 也配置`VSCode`的`launch.json`，可以直接`debugger`启动

### `python`启动

* 默认环境(本地环境`.env`)
```sh
$ python3 main.py  
当前运行环境:  local
2025-01-18 14:29:13.895 | INFO     | __main__:<module>:53 - app_version='v1.0.0' app_env='local' app_name='MT_BINGWALLPAPER' app_host='127.0.0.1' app_port=8000 app_debug=True redis_url='redis://:@127.0.0.1:6379' redis_key_prefix='mt:bingwallpaper:'
INFO:     Will watch for changes in these directories: ['/Users/matias/matias/MT/MTGithub/bingwallpaper']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [40188] using StatReload
当前运行环境:  local
INFO:     Started server process [40190]
INFO:     Waiting for application startup.
2025-01-18 14:29:14.233 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
INFO:     Application startup complete.
```

* 生产环境(`.env.prod`)
```sh
$ python3 main.py --env=prod
当前运行环境:  prod
2025-01-18 14:30:24.402 | INFO     | __main__:<module>:53 - app_version='v1.0.0' app_env='prod' app_name='MT_BINGWALLPAPER' app_host='127.0.0.1' app_port=8000 app_debug=False redis_url='redis://:@127.0.0.1:6379' redis_key_prefix='mt:bingwallpaper:'
INFO:     Will watch for changes in these directories: ['/Users/matias/matias/MT/MTGithub/bingwallpaper']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [40497] using StatReload
当前运行环境:  prod
INFO:     Started server process [40499]
INFO:     Waiting for application startup.
2025-01-18 14:30:24.720 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
INFO:     Application startup complete.
```

**注意** 直接启动，需要注意`python`的地址。
```sh
$ which python3    
/Users/matias/matias/MT/MTGithub/bingwallpaper/venv/bin/python3
```

### `uvicorn`启动

* 默认环境(本地环境`.env`)
```sh
$ uvicorn main:server --port 8000 --env-file .env --reload
$ uvicorn main:server --port 8000 --reload
$ uvicorn main:server --reload
INFO:     Will watch for changes in these directories: ['/Users/matias/matias/MT/MTGithub/bingwallpaper']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [41234] using StatReload
当前运行环境:  local
INFO:     Started server process [41236]
INFO:     Waiting for application startup.
2025-01-18 14:32:27.310 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
INFO:     Application startup complete.
```

* 生产环境(`.env.prod`)
```sh
$ uvicorn main:server --port 8000 --env-file .env.prod
INFO:     Loading environment from '.env.prod'
当前运行环境:  .env.prod
INFO:     Started server process [40923]
INFO:     Waiting for application startup.
2025-01-18 14:31:42.432 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

**提示** `uvicorn`还可以配置其他参数，具体查看[`uvicorn`](http://www.uvicorn.org/settings)文档。

### `gunicorn`启动

* 通过参数启动
```sh
$ gunicorn -w 2 -b 127.0.0.1:8000 -k uvicorn.workers.UvicornWorker main:server
[2025-01-18 14:38:38 +0800] [44167] [INFO] Starting gunicorn 23.0.0
[2025-01-18 14:38:38 +0800] [44167] [INFO] Listening at: http://127.0.0.1:8000 (44167)
[2025-01-18 14:38:38 +0800] [44167] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2025-01-18 14:38:38 +0800] [44209] [INFO] Booting worker with pid: 44209
[2025-01-18 14:38:38 +0800] [44210] [INFO] Booting worker with pid: 44210
当前运行环境:  local
当前运行环境:  local
[2025-01-18 14:38:38 +0800] [44209] [INFO] Started server process [44209]
[2025-01-18 14:38:38 +0800] [44210] [INFO] Started server process [44210]
[2025-01-18 14:38:38 +0800] [44210] [INFO] Waiting for application startup.
[2025-01-18 14:38:38 +0800] [44209] [INFO] Waiting for application startup.
2025-01-18 14:38:38.845 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
2025-01-18 14:38:38.845 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:38:38 +0800] [44210] [INFO] Application startup complete.
[2025-01-18 14:38:38 +0800] [44209] [INFO] Application startup complete.
[2025-01-18 14:38:40 +0800] [44167] [INFO] Handling signal: winch
[2025-01-18 14:38:40 +0800] [44167] [INFO] Handling signal: winch
[2025-01-18 14:38:40 +0800] [44167] [INFO] Handling signal: winch
[2025-01-18 14:38:40 +0800] [44167] [INFO] Handling signal: winch
[2025-01-18 14:38:40 +0800] [44167] [INFO] Handling signal: winch
[2025-01-18 14:38:41 +0800] [44167] [INFO] Handling signal: winch
[2025-01-18 14:38:41 +0800] [44167] [INFO] Handling signal: winch
[2025-01-18 14:38:41 +0800] [44167] [INFO] Handling signal: winch
```

- `-w 4`：指定工作进程的数量。通常，这个数字应该设置为可用`CPU`核心的`2-4`倍。调整这个数字可以优化应用的性能。
- `-b` `127.0.0.1:8000` 服务启动在本地的`8000`端口
- `-k` `uvicorn.workers.UvicornWorker`：指定使用`Uvicorn`的工作类。
- `main:server`：指定应用的模块和应用实例名称。

可以看出上面我们使用了两个工作进程启动服务，输出的启动日志打印了两次，说明两个工作进程都启动了。

* 通过配置文件启动
```sh
$ gunicorn -c gunicorn_config.py main:server
gunicorn -c gunicorn_config.py main:server
[2025-01-18 14:35:17 +0800] [43314] [INFO] Starting gunicorn 23.0.0
[2025-01-18 14:35:17 +0800] [43314] [INFO] Listening at: http://127.0.0.1:8000 (43314)
[2025-01-18 14:35:17 +0800] [43314] [INFO] Using worker: uvicorn.workers.UvicornWorker
[2025-01-18 14:35:17 +0800] [43356] [INFO] Booting worker with pid: 43356
[2025-01-18 14:35:17 +0800] [43357] [INFO] Booting worker with pid: 43357
[2025-01-18 14:35:17 +0800] [43358] [INFO] Booting worker with pid: 43358
[2025-01-18 14:35:17 +0800] [43359] [INFO] Booting worker with pid: 43359
[2025-01-18 14:35:17 +0800] [43360] [INFO] Booting worker with pid: 43360
[2025-01-18 14:35:17 +0800] [43361] [INFO] Booting worker with pid: 43361
[2025-01-18 14:35:17 +0800] [43362] [INFO] Booting worker with pid: 43362
[2025-01-18 14:35:17 +0800] [43365] [INFO] Booting worker with pid: 43365
[2025-01-18 14:35:17 +0800] [43366] [INFO] Booting worker with pid: 43366
当前运行环境:  local
当前运行环境:  local
[2025-01-18 14:35:17 +0800] [43367] [INFO] Booting worker with pid: 43367
[2025-01-18 14:35:17 +0800] [43368] [INFO] Booting worker with pid: 43368
[2025-01-18 14:35:17 +0800] [43356] [INFO] Started server process [43356]
[2025-01-18 14:35:17 +0800] [43356] [INFO] Waiting for application startup.
2025-01-18 14:35:17.893 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:17 +0800] [43356] [INFO] Application startup complete.
[2025-01-18 14:35:17 +0800] [43369] [INFO] Booting worker with pid: 43369
[2025-01-18 14:35:17 +0800] [43357] [INFO] Started server process [43357]
[2025-01-18 14:35:17 +0800] [43357] [INFO] Waiting for application startup.
[2025-01-18 14:35:17 +0800] [43370] [INFO] Booting worker with pid: 43370
2025-01-18 14:35:17.944 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:17 +0800] [43357] [INFO] Application startup complete.
当前运行环境:  local
[2025-01-18 14:35:18 +0800] [43371] [INFO] Booting worker with pid: 43371
[2025-01-18 14:35:18 +0800] [43372] [INFO] Booting worker with pid: 43372
[2025-01-18 14:35:18 +0800] [43373] [INFO] Booting worker with pid: 43373
[2025-01-18 14:35:18 +0800] [43374] [INFO] Booting worker with pid: 43374
当前运行环境:  local
[2025-01-18 14:35:18 +0800] [43358] [INFO] Started server process [43358]
[2025-01-18 14:35:18 +0800] [43358] [INFO] Waiting for application startup.
当前运行环境:  local
当前运行环境:  local
2025-01-18 14:35:18.331 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43358] [INFO] Application startup complete.
当前运行环境:  local
[2025-01-18 14:35:18 +0800] [43359] [INFO] Started server process [43359]
[2025-01-18 14:35:18 +0800] [43359] [INFO] Waiting for application startup.
当前运行环境:  local
当前运行环境:  local
[2025-01-18 14:35:18 +0800] [43362] [INFO] Started server process [43362]
[2025-01-18 14:35:18 +0800] [43362] [INFO] Waiting for application startup.
2025-01-18 14:35:18.469 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43362] [INFO] Application startup complete.
2025-01-18 14:35:18.474 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43359] [INFO] Application startup complete.
[2025-01-18 14:35:18 +0800] [43360] [INFO] Started server process [43360]
[2025-01-18 14:35:18 +0800] [43360] [INFO] Waiting for application startup.
2025-01-18 14:35:18.512 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43360] [INFO] Application startup complete.
当前运行环境:  local
当前运行环境:  local
当前运行环境:  local
[2025-01-18 14:35:18 +0800] [43365] [INFO] Started server process [43365]
[2025-01-18 14:35:18 +0800] [43365] [INFO] Waiting for application startup.
当前运行环境:  local
2025-01-18 14:35:18.600 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43361] [INFO] Started server process [43361]
[2025-01-18 14:35:18 +0800] [43361] [INFO] Waiting for application startup.
当前运行环境:  local
[2025-01-18 14:35:18 +0800] [43365] [INFO] Application startup complete.
[2025-01-18 14:35:18 +0800] [43366] [INFO] Started server process [43366]
[2025-01-18 14:35:18 +0800] [43366] [INFO] Waiting for application startup.
当前运行环境:  local
2025-01-18 14:35:18.641 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43366] [INFO] Application startup complete.
2025-01-18 14:35:18.651 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43361] [INFO] Application startup complete.
当前运行环境:  local
当前运行环境:  local
[2025-01-18 14:35:18 +0800] [43367] [INFO] Started server process [43367]
[2025-01-18 14:35:18 +0800] [43367] [INFO] Waiting for application startup.
2025-01-18 14:35:18.701 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43367] [INFO] Application startup complete.
[2025-01-18 14:35:18 +0800] [43370] [INFO] Started server process [43370]
[2025-01-18 14:35:18 +0800] [43370] [INFO] Waiting for application startup.
[2025-01-18 14:35:18 +0800] [43368] [INFO] Started server process [43368]
[2025-01-18 14:35:18 +0800] [43368] [INFO] Waiting for application startup.
[2025-01-18 14:35:18 +0800] [43369] [INFO] Started server process [43369]
[2025-01-18 14:35:18 +0800] [43369] [INFO] Waiting for application startup.
2025-01-18 14:35:18.721 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43370] [INFO] Application startup complete.
[2025-01-18 14:35:18 +0800] [43372] [INFO] Started server process [43372]
[2025-01-18 14:35:18 +0800] [43372] [INFO] Waiting for application startup.
2025-01-18 14:35:18.738 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
2025-01-18 14:35:18.738 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43368] [INFO] Application startup complete.
[2025-01-18 14:35:18 +0800] [43369] [INFO] Application startup complete.
[2025-01-18 14:35:18 +0800] [43374] [INFO] Started server process [43374]
[2025-01-18 14:35:18 +0800] [43374] [INFO] Waiting for application startup.
[2025-01-18 14:35:18 +0800] [43371] [INFO] Started server process [43371]
[2025-01-18 14:35:18 +0800] [43371] [INFO] Waiting for application startup.
2025-01-18 14:35:18.754 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43372] [INFO] Application startup complete.
[2025-01-18 14:35:18 +0800] [43373] [INFO] Started server process [43373]
[2025-01-18 14:35:18 +0800] [43373] [INFO] Waiting for application startup.
2025-01-18 14:35:18.758 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43374] [INFO] Application startup complete.
2025-01-18 14:35:18.766 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43371] [INFO] Application startup complete.
2025-01-18 14:35:18.769 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
[2025-01-18 14:35:18 +0800] [43373] [INFO] Application startup complete.
[2025-01-18 14:35:21 +0800] [43314] [INFO] Handling signal: winch
[2025-01-18 14:35:21 +0800] [43314] [INFO] Handling signal: winch
[2025-01-18 14:35:21 +0800] [43314] [INFO] Handling signal: winch
[2025-01-18 14:35:21 +0800] [43314] [INFO] Handling signal: winch
[2025-01-18 14:35:21 +0800] [43314] [INFO] Handling signal: winch
[2025-01-18 14:35:21 +0800] [43314] [INFO] Handling signal: winch
[2025-01-18 14:35:21 +0800] [43314] [INFO] Handling signal: winch
[2025-01-18 14:35:21 +0800] [43314] [INFO] Handling signal: winch
[2025-01-18 14:35:21 +0800] [43314] [INFO] Handling signal: winch
[2025-01-18 14:35:21 +0800] [43314] [INFO] Handling signal: winch
```

关闭服务，关闭信息也打印了两次：
```sh
$ ^C
[2025-01-18 14:40:35 +0800] [44167] [INFO] Handling signal: int
[2025-01-18 14:40:35 +0800] [44209] [INFO] Shutting down
[2025-01-18 14:40:35 +0800] [44210] [INFO] Shutting down
[2025-01-18 14:40:35 +0800] [44210] [INFO] Waiting for application shutdown.
[2025-01-18 14:40:35 +0800] [44209] [INFO] Waiting for application shutdown.
2025-01-18 14:40:35.613 | INFO     | app.server.app_server:lifespan:33 - Redis close
2025-01-18 14:40:35.613 | INFO     | app.server.app_server:lifespan:33 - Redis close
[2025-01-18 14:40:35 +0800] [44209] [INFO] Application shutdown complete.
[2025-01-18 14:40:35 +0800] [44210] [INFO] Application shutdown complete.
[2025-01-18 14:40:35 +0800] [44209] [INFO] Finished server process [44209]
[2025-01-18 14:40:35 +0800] [44210] [INFO] Finished server process [44210]
[2025-01-18 14:40:35 +0800] [44167] [ERROR] Worker (pid:44210) was sent SIGINT!
[2025-01-18 14:40:35 +0800] [44167] [ERROR] Worker (pid:44209) was sent SIGINT!
[2025-01-18 14:40:35 +0800] [44167] [INFO] Shutting down: Master
```

## 部署

### 云服务器部署

创建虚拟环境
```sh
$ python3 -m venv venv
```

进入虚拟环境
```sh
$ source venv/bin/activate
(venv) root@iZ7xvfrafhk3mj9ma5nn6lZ:~#
```

安装`requirements.txt`依赖
```sh
$ pip3 install -r requirements.txt
```

确认端口是否被占用
```sh
$ lsof -i:8000
```
没有显示使用了这个端口，则可以在这个端口上面部署。

使用`uvicorn`测试环境运行
```sh
$ uvicorn main:server --port 8000 --env-file .env.test --reload
INFO:     Will watch for changes in these directories: ['/var/mt-modules/bingwallpaper']
INFO:     Loading environment from '.env.test'
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2639586] using StatReload
当前运行环境:  .env.test
INFO:     Started server process [2639588]
INFO:     Waiting for application startup.
2024-04-26 17:19:06.381 | INFO     | app.server.app_server:lifespan:29 - Redis 挂载（redis://:@127.0.0.1:6379）：成功
INFO:     Application startup complete.
```

也可以选择后台运行项目
```sh
$ nohup uvicorn main:server --port 8000 --env-file .env.test >>output.out 2>&1 &
[1] 2639974
```

查看服务
```sh
$ ps -ef | grep uvicorn
root     2639974 2638464  2 17:36 pts/0    00:00:01 /root/kk-aippt/bin/python3 /root/kk-aippt/bin/uvicorn main:server --port 8000 --env-file .env.test
root     2639992 2638464  0 17:37 pts/0    00:00:00 grep --color=auto uvicorn
```

查询服务
```sh
$ ps -ef | grep uvicorn | grep -v grep | awk '{print $2}'
2639974
```

退出虚拟环境
```sh
$ deactivate
```

### `Docker`镜像

本项目也配置了`Dockerfile`文件，可以使用下面的命令，打包`Docker`镜像。
```sh
$ docker build -t bingwallpaper --network=host .
```

## 版本说明

### v1.0.3

- 更新版本号为v1.0.3
- 新增`/random/{n}`接口，随机返回最近`n`张壁纸种的一张

### v1.0.2

- 更新说明文档。

### v1.0.1

- 更新说明文档，添加项目部署后的测试链接。

### v1.0.0

- 实现接口转发到微软必应最新背景图功能。

## 参考

[获取今日微软bing壁纸](https://api.tdytech.cn/api/wallpaper/bing/last)

[获取微软必应每日背景图](https://matiastang.github.io/article/y7liklme.html)

[Python项目如何优雅的生成依赖文件](https://matiastang.github.io/article/yukb34ys.html)

[Python 格式自动修复](https://matiastang.github.io/article/u1og7vsz.html)

[Python 格式校验](https://matiastang.github.io/article/y8faf61c.html)

[整理头文件](https://matiastang.github.io/article/94w8v0n3.html)

[bing](https://cn.bing.com)