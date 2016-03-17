#!/usr/bin/env python
# -*- coding: utf-8 -*-
def isPrime(N):
    count=0
    for i in range(2,N+1):
        if N%i==0:
            count=count+1
    if count==1:
       return 1
    else:
      return 0
add=0
for j in range(2,1001):
	if(isPrime(j)):
		add+=j
print "2~1000中所有質數和=%d" %add