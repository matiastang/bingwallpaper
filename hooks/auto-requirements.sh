#!/bin/zsh
###
 # @Author: matiastang
 # @Date: 2024-05-13 17:48:01
 # @LastEditors: matiastang
 # @LastEditTime: 2024-05-13 18:27:50
 # @FilePath: /mt-langchain/hooks/auto-requirements.sh
 # @Description: auto requirements
### 
# 生成requirements.txt
pip3 freeze > ./requirements.txt