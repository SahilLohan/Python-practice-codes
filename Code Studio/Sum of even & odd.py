#Link for problem :- https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118792/offering/1461390?leftPanelTab=0

#Code --->

N=int(input())
even = 0
odd = 0
while(N>0):
    rem=int(N%10)
    N=N/10
    if int(rem%2)==0:
        even=even+rem
    else:
        odd=odd+rem

print(str(even)+" "+str(odd))
