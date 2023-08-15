#!/bin/bash

# 定义包含三个字符串元素的数组
fruits=("apple" "banana" "orange")

# 使用循环遍历输出数组元素
for fruit in "${fruits[@]}"; do
    echo "$fruit"
done

# 清空终端缓冲并立即显示输出
#echo -e "\033[0m"

