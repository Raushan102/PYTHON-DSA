#https://leetcode.com/problems/last-substring-in-lexicographical-order/

# youtube channel to understand this question https://www.youtube.com/watch?v=4ZlnVK16sH8
class Solution(object):
    def lastSubstring(self, s):
        
        i=0
        j=1
        k=0

        while i+k < len(s):
            if s[i+k] == s[j+k]:
                k+=1
            elif s[i+k] > s[j+k]:
                j=j+k+1
                k=0
            else:
                if i+k+1 > j:
                    i=i+k+1
                else:
                    i=j
                j=i+1
                k=0
        return s[i:]


        