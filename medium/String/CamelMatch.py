# https://leetcode.com/problems/camelcase-matching/

class Solution(object):
    def camelMatch(self, queries, pattern):
        k=0
        while k < len(queries):
            i=0
            j=0
            while i < len(queries[k]) and j < len(pattern):
                item=queries[k]
                if item[i] == pattern[j]:
                    i+=1
                    j+=1
                elif ord("A") <= ord(item[i]) <=ord("Z"):
                    queries[k]=False
                    break
                else:
                    i+=1
            if j==len(pattern):
                while i < len(item):
                    if ord("A") <= ord(item[i]) <=ord("Z"):
                        queries[k]=False
                        break
                    i+=1
                if i==len(item) and queries[k]!=False:
                    queries[k]=True  
            else:
                queries[k]=False  
            k+=1
        return queries
          
      

sol=Solution()

print(sol.camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"],"FoBa"))