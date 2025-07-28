
#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def strStr( haystack, needle):
    n=len(haystack)
    if needle in haystack:
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                j=0
                d=0
                while j < len(needle):
                    if i+j < n and haystack[i+j]==needle[j]:
                        d+=1
                        j+=1
                    else:
                        break
                if d==len(needle):
                    return i
                else:
                    i=j

    else:
        return -1


print(strStr("mississippi","issip"))