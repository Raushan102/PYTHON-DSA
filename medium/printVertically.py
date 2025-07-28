#https://leetcode.com/problems/print-words-vertically/
class Solution(object):
    def printVertically(self, s):
        #find the max len of string in string s
        s=s.split(" ")
        length=len(s[0])
        for item in s:
            if length < len(item):
                length=len(item)
        
        i=0
        arr=[0]*length
        index=0

        while i < length:
            
            j=0
            
            while j < len(s):
                item=s[j]
                if i >=len(item):
                    temp=" "
                else:
                    temp=item[i]

                if arr[index]==0:
                    arr[index]=temp 
                else:
                    arr[index]+=temp
                
                j+=1
            
            
            d=list(arr[index])
            l=len(d)-1
            while l >= 0 and d[l]==" ":
              d.pop()
              l=len(d)-1
            d=''.join(d)
            arr[index]=d 

            index+=1  
            i+=1       
        return arr
    
       
sol=Solution()
print(sol.printVertically("AA BBB C DDDD EEEEE F"))