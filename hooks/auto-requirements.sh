#!/bin/zsh
###
 # @Author: matiastang
 # @Date: 2024-05-13 17:48:01
 # @LastEditors: matiastang
 # @LastEditTime: 2024-05-13 18:27:50
 # @FilePath: /mt-langchain/hooks/auto-requirements.sh
 # @Description: auto requirements
### 

# 检查是否存在虚拟环境
if [ -f "./venv/bin/activate" ]; then
    # 使用项目虚拟环境
    source ./venv/bin/activate
    pip3 freeze > ./requirements.txt
    deactivate
elif [ -n "$VIRTUAL_ENV" ]; then
    # 如果当前已在虚拟环境中
    pip3 freeze > ./requirements.txt
else
    # 没有虚拟环境时，跳过更新requirements.txt以避免污染
    echo "警告: 未检测到虚拟环境，跳过requirements.txt更新"
    echo "请激活虚拟环境或创建./venv/虚拟环境后再运行"
    exit 0
fi