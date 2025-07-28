class Solution(object):
    def nextGreaterElement(self, n):
        if n > 2147483647:   # check weather number is out of range of integer or not 
            return -1

        n=list(str(n))

        j=len(n)-1

        temp_array=[]

        while j > 0 :     # traverse from last and separate the max ele from last 
            if n[j-1] >= n[j] :
                temp_array.append(n[j])
                n.pop(j)
                j-=1
            else:
                break
        if j <=0:
            return -1
        
        temp_array.append(n[j]) 
        n.pop(j)
        j-=1
        temp_array.sort()

        i=0

        while i < len(temp_array):
             if temp_array[i] > n[j]:   # swap with next grater element 
                 temp_array[i],n[j]=n[j],temp_array[i]
                 break
             else:
                 i+=1

        if int((''.join(n))+''.join(temp_array)) > 2147483647:  # check weather output is out of range or not
            return -1 
            
        
        return int((''.join(n))+''.join(temp_array))
        

sol=Solution()
print(sol.nextGreaterElement(21))