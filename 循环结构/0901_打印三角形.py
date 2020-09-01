# _*_ coding: utf-8 _*_
# @Time : 2020/9/1 9:38 上午 
# @Author : Hank 
# @Version：V 0.1
# @File : 0901_打印三角形.py
# @desc :打印三角形图案

row = int(input('请输入行数：'))

for i in range(row):
    for _ in range(i+1):
        print('*',end='')
    print()

