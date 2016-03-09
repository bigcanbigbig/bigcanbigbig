#!/usr/bin/env python
# -*- coding: utf-8 -*-
num=raw_input('你要領多少錢呢:')
want=int(num)
money=5000

f=open("ATM.txt","a")

if money>want:
    print "你的存款還剩%d元" %(money-want)
    f.write("你的存款還剩%d元\n"%(money-want))
elif want==money:
    print "你沒錢了"
    f.write("你沒錢了\n")
else:
    print "錢不夠啦笨蛋"
    f.write("錢不夠啦笨蛋\n")

f.close
