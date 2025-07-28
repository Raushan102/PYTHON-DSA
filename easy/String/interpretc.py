#https://leetcode.com/problems/goal-parser-interpretation/

def interpret(command):
    resultString=""
    for i in range(len(command)):
        if command[i]== "(" and command[i + 1]== ")":
            resultString+="o"
        elif command[i]== "(" or command[i]== ')':
            continue
        else:
            resultString+=command[i]

    return resultString

print(interpret("G()(al)"))