# python版本
FROM python:latest

# 信息
LABEL version="0.0.1"
LABEL maintainer="matiastang"
LABEL description="MT_BINGWALLPAPER"

# 设置时间
RUN ln -sf /usr/share/zoneinfo/Asia/Beijing/etc/localtime

# 输出时间
RUN echo 'Asia/Beijing' >/etc/timezone

# 设置工作目录
WORKDIR /code

# 复制该文件到工作目录中
COPY ./requirements.txt /code/requirements.txt

# 禁用缓存并批量安装包
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 复制代码到工作目录（**注意** 这里使用的是.env配置文件）
COPY ./main.py /code/main.py
COPY ./.env /code/.env
COPY ./app /code/app

# 放开端口
EXPOSE 80

# 命令行运行，启动uvicorn服务，指定ip和端口(--reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。)
CMD ["uvicorn", "main:server", "--reload", "--host", "0.0.0.0", "--port", "80"]

# 输出提示
RUN echo 'MT_BINGWALLPAPER images build ok!'