#https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution(object):
    def minimumLength(self, s):
        str_array=list(s)
        
        i=0
        j=len(str_array)-1

        while i<j:
            if str_array[i]==str_array[j]:
                while i+1 < len(str_array) and str_array[i]==str_array[i+1]:
                       i+=1
                while j-1 >=0  and str_array[j]==str_array[j-1]:
                       j-=1
                str_array=str_array[i+1:j]
                j=len(str_array)-1
                i=0
            else:
                return len(str_array)
        return len(str_array)
    
sol=Solution()

print(sol.minimumLength("aabccabba"))



            
            
            
            
            
        
        