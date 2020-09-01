# _*_ coding: utf-8 _*_
# @Time : 2020/9/1 9:03 上午 
# @Author : Hank 
# @Version：V 0.1
# @File : 0901_猜数字游戏.py
# @desc :

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')