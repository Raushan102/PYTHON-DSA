def checkPalindromeFormation( a, b):

  def isPalindrome(string ,i ,j):
    while i < j and string[i]==string[j]:
      i+=1
      j-=1
    return i>=j
      
  
  def check(a ,b):
    i=0
    j=len(b)-1
    
    while i<j and a[i]==b[j]:
      i+=1
      j-=1
    else:
      return isPalindrome(a,i,j) or isPalindrome(b,i,j)
  
  return check(a,b) or check(b,a)

print(checkPalindromeFormation("ulacfd","jizalu"))
