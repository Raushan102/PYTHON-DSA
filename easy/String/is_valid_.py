#https://leetcode.com/problems/valid-parentheses/

def isValid( s):
    brackets=list(s)
    bracketsStack=[]


    for i in range(len(brackets)):

        if brackets[i] == ")" or brackets[i]=="}" or brackets[i] == "]":

            if brackets[i] == bracketsStack[len(bracketsStack)-1]:
                bracketsStack.pop()
            else:
                return False

        else:
            bracketsStack.append(brackets[i])

    return len(bracketsStack)==0



print(isValid("()"))