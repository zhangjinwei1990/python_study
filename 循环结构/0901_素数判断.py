# _*_ coding: utf-8 _*_
# @Time : 2020/9/1 9:22 上午 
# @Author : Hank 
# @Version：V 0.1
# @File : 0901_素数判断.py
# @desc : 输入一个正整数判断是不是素数

num = int(input('请输入一个正整数：'))
end = int(num)

is_prime = True
for x in range(2, end):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('{0}是素数'.format(num))
else:
    print('{0}不是素数'.format(num))
