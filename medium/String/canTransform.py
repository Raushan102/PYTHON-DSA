#https://leetcode.com/problems/swap-adjacent-in-lr-string/

class Solution(object):
    def canTransform(self, start, result):
          # after removing the X both string should be same 
          if start.replace("X","") != result.replace("X",""): return False
          i=0 
          j=0
          while i< len(start) and j <len(result):
               if start[i]=="X":i+=1
               elif result[j]=="X":j+=1
               else: 
                    # we can only move L in the left but if it present in left side already then this is not valid string 
                    # similar with R we can only move R in the right side but in it occur in right then it is not  valid
                    if start[i]=="L" and i < j or start[i]=="R" and i > j: return False
                    i+=1
                    j+=1
          return True
                         
sol=Solution()
print(sol.canTransform("L","R"))
                
                    
                    

                        
        