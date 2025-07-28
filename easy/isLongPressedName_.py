#https://leetcode.com/problems/long-pressed-name/
from pyexpat import native_encoding


def isLongPressedName(name, typed):
    i=0
    j=0

    while j < len(typed) and i < len(name):

        if name[i]== typed[j]:
                i+=1
                j+=1
        elif i-1 >=0 and name[i - 1]== typed[j]:
                j+=1
        else:
            return False

    if i< len(name):
        return False

    if j< len(typed):
        while j< len(typed):
            if name[len(name)-1] != typed[j]:
                return False
            else:
                j+=1

    return True





print(isLongPressedName("pyplrz","ppyypllr"))