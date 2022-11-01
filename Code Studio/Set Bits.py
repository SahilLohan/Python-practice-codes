# Link for problem :- https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118793/offering/1461399

# code --->

from os import *
from sys import *
from collections import *
from math import *

def countBits(n):
    count=0
    x=1
    while n!=0:
        if n%(2)==1:
            count+=1
            n=n-1
        else:
            n=n//2
    return count
        
n = int(input())
print(countBits(n))

