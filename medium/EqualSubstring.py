#https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        max_length=0

        current_result=0
        i=0
        j=0

        while j < len(t):
            temp=abs(ord(t[j])- ord(s[j]))
            current_result+=temp
            
            while i <= j and current_result > maxCost:
                if (j-i > max_length):
                    max_length=j-i
                temp= abs(ord(t[i])-ord(s[i]))
                current_result-=temp
                i+=1
            j+=1
        return max_length

sol=Solution()

print(sol.equalSubstring("krrgw","zjxss",19))

            
        