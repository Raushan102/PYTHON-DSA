#https://leetcode.com/problems/maximum-number-of-removable-characters/

class Solution(object):
    def maximumRemovals(self, s, p, removable):
         s=list(s)
         p=list(p)
         start=0
         end=len(removable)-1

         while start<= end:
             mid= start+(end-start)//2
             temp_s=s[:]
             temp= 0

             while temp <= mid:
                 temp_s[removable[temp]]="0"
                 temp+=1
             
             if subSetChecker(temp_s,p):
                 start=mid+1
             else:
                 end=mid-1
         return end+1
    
     
def subSetChecker(s,p):
        i = 0
        j=0

        while i < len(p) and j < len(s):
            
            if (p[i] == s[j] ):
                i+=1
                j+=1
            else:
                j+=1
        else:
             if i >=len(p):
                 return True
             else:
                 return False

sol=Solution()

print(sol.maximumRemovals("abcacb","ab",[3,1,0]))
             
        