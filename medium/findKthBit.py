
#https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/

class Solution(object):
    def findKthBit(self, n, k):
        str="0"
        i=1

        while i < n:
            str2=str

            if len(str2) >= k:
                return str2[k-1]
            
            str2=str2+"1"

            str=list(str)

            for j in  range(len(str)):
                if str[j]=="0":
                    str[j]="1"
                else:
                    str[j]="0"
            
            str=str[::-1]

            str="".join(str)

            str=str2+str
            i+=1
        
        return str[k]

sol=Solution()

print(sol.findKthBit(4,1))

            
        