# print all subsets of a list
# lets use recursion



ans=list()

def solve(list1,length,index=0):
    global ans
    
    if index==length:
        print(ans)
    else:
        # with an element choosen
        ans.append(list1[index])
        solve(list1,length,index+1)
        ans.pop(-1)
        # without that current element
        solve(list1,length,index+1)
        
    
arr=[1,2,3,4]
solve(arr,len(arr))
