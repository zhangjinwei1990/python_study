# _*_ coding: utf-8 _*_
# @Time : 2020/9/1 9:08 上午 
# @Author : Hank 
# @Version：V 0.1
# @File : 0901_九九乘法表.py
# @desc : 输出九九乘法表

for i in range(1, 10):
    for j in range(1, 10):
        print('{0} * {1} = {2}'.format(i, j, i * j), end='\t')
    print()  # 和 print('\r')  效果一样，在一个循环结束后换行
