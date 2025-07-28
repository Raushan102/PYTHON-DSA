def  IsPalindrome(str):
    start=0
    end=len(str)-1
    while start < end:
        if str[start] != str[end]:
            return False
        else:
            start+=1
            end-=1
    return True


print(IsPalindrome("qwewq"))