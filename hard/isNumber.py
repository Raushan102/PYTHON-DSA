#https://leetcode.com/problems/valid-number/

class Solution(object):
    def isNumber(self, s):

        numberSeen=False
        dotSeen=False
        eSeen=False
        n=len(s)

        for i in range(len(s)):
            c_element=s[i]

            if c_element == '+' or c_element=='-':
                 
                # operator always comes at the start or after the e this is the two position of the operator in the number else not valid number
                # -34 valid
                # 34E+34 valid
                # 23E+ ❌ because after + number not present it comes at the end  not valid and according to e rule it not allowed
                # 23++ ❌ not allowed

                if not(i==0) and s[i-1]!= "e" and s[i-1] !="E":
                    return False
                numberSeen=False  # i do numberSeen false because we need number after - or + because - , + should not come at  the end like 12+,23++,45E+
                                  #  and here i am returning numberSeen at the end that why i make false means if we not seen the number after - and + 
                                  # then it always false and when i return the numberSeen  that is false but if we get any number it become true and we 
                                  # true
                
                # in one number 2 dots not allowed 3..4 ❌ 
                # after e dot not allowed e3.4 ❌

            elif c_element == ".":
                if dotSeen or eSeen :
                    return False
                dotSeen=True    # note= here i not doing numberSeen = false because . can present at end like 23. valid so we don't need to make False

                # e or E should not present at start or and in  one number two  e or E not allow it always comes b/w numbers after e can contain + or - then after number   
                # e87 not valid because e at start of number
                # 23E not valid number because E at end 
                # 23e+ not valid number because after e number not present 
                #23e+23 valid number because before e and after e number are present

            elif c_element=="e" or c_element=='E' :
                if not(numberSeen) or eSeen or i==n-1:
                    return False 
                eSeen=True
                numberSeen=False # same reason i already mention above after e we also need number like 23E ❌ or 23E+❌
            elif isdigit(c_element):
                numberSeen=True  # if we get number then it become True
            else:
                return False     # if number contain other then -,+,e,. then it not valid number
        return numberSeen
   
        return True

def isdigit(chr):
    if (48 <= ord(chr) <=57 ):
        return True
    else:
        return False
  
sol=Solution()


print(sol.isNumber("+86"))




            
                    
              
                      
                

            
            



