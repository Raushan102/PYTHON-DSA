#https://leetcode.com/problems/basic-calculator/
class Solution(object):
    def calculate(self, s):
        result=0
        operator=1
        number=0
        
        arr=[]

        s=list(s)
        for i in range(len(s)):
            if (s[i]=="("):
                result+=number*operator
               
                arr.append(result)
                result=0
                arr.append(operator)
                number=0
                operator=1
            elif s[i]=="+":
                result+=number*operator
                number=0
                operator=1
            elif s[i]=="-":
                result+=number*operator
                number=0
                operator=-1
            elif s[i]==")":
                result+=operator*number
                number=0
                result=result*arr.pop()
                result+=arr.pop()
            elif s[i]==" ":
                continue
            else:
                digit=ord(s[i])-ord('0')
                number=number*10+digit
        result+=operator*number
        return result         

                
                
sol=Solution()
print(sol.calculate("- (3 + (4 + 5))"))