# -*- coding: utf-8 -*-

get=raw_input('請輸入一正整數：')
num=int(get)
def isprime(a):
    count=0
    for i in range(2,a+1):
        if a%i==0:
            count=count+1
    if count==1:
       return 1
    else:
      return 0
if isprime(num):
    print '%d是質數' %num
else:
    print '%d不是質數' %num
