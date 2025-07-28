# https://leetcode.com/problems/shifting-letters/

class Solution(object):
    def shiftingLetters(self, s, shifts):
        sum=0
        str=list(s)
        i=len(shifts)-1
        while i >= 0:
            sum+=shifts[i]        
            shifts[i]=sum            
            temp=ord(str[i])-97
            temp2=(temp+shifts[i])%26
            str[i]=chr(97+temp2)
            i-=1
        
        return ''.join(str)
    
sol=Solution()
print(sol.shiftingLetters("ruu",[26,9,17]))