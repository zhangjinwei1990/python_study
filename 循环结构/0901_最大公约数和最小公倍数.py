# _*_ coding: utf-8 _*_
# @Time : 2020/9/1 9:27 上午 
# @Author : Hank 
# @Version：V 0.1
# @File : 0901_最大公约数和最小公倍数.py
# @desc : 输入两个正整数，计算它们的最大公约数和最小公倍数
# tips:两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。

x = int(input('请输入正整数x：'))
y = int(input('请输入正整数y：'))
# 如果x大于y，则交换x,y的值（因为循环里是以x作为循环基数，应使用两数较小的一个数）
if x > y:
    # 直接以下面操作进行x,y交换
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('{0}和{1}的最大公约数是{2}'.format(x, y, factor))
        print('{0}和{1}的最小公倍数是{2}'.format(x, y, x * y // factor))
        break
