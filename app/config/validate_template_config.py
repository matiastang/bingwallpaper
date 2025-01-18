'''
Author: matiastang
Date: 2024-03-12 18:01:13
LastEditors: matiastang
LastEditTime: 2024-04-23 17:09:26
FilePath: /bingwallpaper/app/config/validate_template_config.py
Description: 校验模板配置
'''
# 错误模版
validateChineseDict = {
    "value_error.number.not_gt": "{},值不能大于:{}",
    "value_error.number.not_ge": "{},值不能小于等于:{}",
    "value_error.list.min_items": "{},元素个数至少为:{}",
    "value_error.str.regex": "{},不满足规则:{}"
}

# 关键词显示的错误
keyErrorChineseDict = {
    "phone": "手机号格式不正确~"
}
