#Link for problem :- https://www.codingninjas.com/codestudio/guided-paths/basics-of-python/content/118792/offering/1461392?leftPanelTab=0

#Code --->

x=int(input())
ans=1
if x>0:
    for i in range(1,x+1):
        ans*=i

    print(str(ans))
elif x==0:
    print("1")

else:
    print("Error")
