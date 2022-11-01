// Link :- https://leetcode.com/problems/length-of-last-word/description/


// code --->


class Solution(object):
    def lengthOfLastWord(self, s):
        n=len(s)
        while s[n-1]==" ":
            n=n-1

        count=0
        while s[n-1]!=" ":
            if n==0:
                break
            count= count+1
            n=n-1
            

        return count
