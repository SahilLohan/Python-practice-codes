# Link for problem :- https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118793/offering/1461396

# code --->

from os import *
from sys import *
from collections import *
from math import *

#Write your printDivisors function here.

def printDivisors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(str(i),end=" ")


n = int(input())
printDivisors(n)
