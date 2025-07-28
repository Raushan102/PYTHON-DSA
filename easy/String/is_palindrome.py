#https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s):
     str=list(s)
     result=""
     for i in range(len(str)):
         print(ord(str[i]))
         if (65 <= ord(str[i]) <= 90) or (122 >= ord(str[i]) >= 97) or (57 >=ord(str[i]) >= 48):
             result+=str[i]
     i=0
     j=len(result)-1
     result=result.lower()
     print(result)
     while i<=j:
        if result[i] !=result[j]:
            return False
        else:
            i+=1
            j-=1
     return True

print(isPalindrome("0P"))


