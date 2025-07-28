#https://leetcode.com/problems/multiply-strings/

# this problem is bout write a algorithm to perform the multiplication like we do on paper
# both number are string we have to convert the string to int without using built in function 

class Solution(object):
    def multiply(self, num1, num2):
        
        i =len(num1)-1
        
        # create array to store result
        arr=[0 for _ in range(len(num1)+len(num2))]

        while i >= 0 :
            j=len(num2)-1
            while j >=0:
                
                # convert the string in number and multiply them
                digit=ord(num1[i])-ord('0')
                digit2=ord(num2[j])-ord('0')
                mul=digit*digit2  
                # calculate the insert position
                pos_low=i+j+1
                pos_high=i+j

                sum=mul+arr[pos_low]
                arr[pos_low]=sum%10  # pick first last position integer from integer
                arr[pos_high]+=sum//10  # add the carry
                j-=1
            i-=1
        finalResult=""
        allZero=True
        if arr[0]== 0:    # if first position contain zero then replace it with ""
            arr[0]=""
        for item in arr:  #  convert integer array to string
            if allZero and  item ==0 or item=="": # check all numbers are Zero or not if yes then return single Zero
                allZero=True
            else:
                allZero=False
            finalResult+=str(item)

        if allZero==True: # if all number are Zero then return single Zero
            finalResult="0"   
        return   finalResult

    
sol=Solution()
print(sol.multiply("123","0"))

                
       
        
