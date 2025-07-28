#https://leetcode.com/problems/valid-palindrome-ii/

def validPalindrome(s):
    i=0
    j=len(s)-1


    while i<=j:
        print(s[j])

        if s[i]!=s[j]:

                if j-1 >=0 and helper_palindrome_function(i,j-1,s):
                    return True
                elif i+1 < len(s) and helper_palindrome_function(i+1,j,s):
                    return True
                else:
                    return False
        else:
            i+=1
            j-=1
    return True

def helper_palindrome_function(i,j,s):

    while i<=j:
        if s[i] != s[j]:
          return False
        else:
          i+=1
          j-=1
    else:
        return True


print(validPalindrome("eceec"))
