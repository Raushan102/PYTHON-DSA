#https://leetcode.com/problems/to-lower-case/

def toLowerCase(s):
    s=list(s)
    for i in range(len(s)):
        asciiValu=ord(s[i])
        if asciiValu >= 65 and asciiValu <=90:
            temp=asciiValu-65
            s[i]=chr(97+temp)
    return ''.join(s)









print(toLowerCase("HELLOZA"))