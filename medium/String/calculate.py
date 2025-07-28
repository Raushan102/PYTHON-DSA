
class Solution(object):
    def calculate(self, s):
        
        exp_char=list(s)
        arr=[]
        current=0
        operator="+"

        for i in range(len(exp_char)):
            if is_digit(exp_char[i]):
                number=ord(exp_char[i])-ord("0")
                current=(current*10)+number
                
            
            if not(is_digit(exp_char[i])) and exp_char[i]!=" " or i== (len(exp_char)-1):
                if operator=="+":
                    arr.append(current)
                elif operator=="-":
                    arr.append(-current)
                elif operator=="/":
                    arr.append(int(arr.pop()/current))
                elif operator=="*":
                    arr.append(arr.pop()*current)
                current=0
                operator=exp_char[i]
            
        result=0
        i=0
        while i < len(arr):
            result+=arr[i]
            i+=1
        return result


def is_digit(char):
    ASCII_number=ord(char)

    if(ASCII_number < 48):
        return False
    else:
        return True


sol=Solution()

print(sol.calculate("14-3/2"))
