# Link for problem :- https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118793/offering/1461401?leftPanelTab=0

# code --->

def isPrime(i):
    if i<2:
        return 1
    for x in range(2,i):
        if i%x==0:
            return 0
    return 1

#Write your totalPrime function here
def totalPrime(S,E):
    count=0
    for i in range(S,E+1):
        if isPrime(i)==1:
            count+=1
    return count

#Taking S and E space seperated input.
S,E = map(int,input().split(' '))
print(totalPrime(S,E))


