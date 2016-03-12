# -*- coding: utf-8 -*-

f=open("index.txt","r")

space=0
e=0
n=0
count=0
word=f.read()
for x in word:
        if x==' ':
                space+=1
        if x=='e':
                e+=1
        if x=='\n':
                n+=1
        count+=1
all=count-n
print 'space:%d' %space
print 'percentage of space:%f' %(float(space)/float(all))
print 'e:%d' %e
print 'percentage of e:%f' %(float(e)/float(all))
print 'all:%d' %all
