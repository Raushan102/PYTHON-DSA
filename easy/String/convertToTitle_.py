#https://leetcode.com/problems/excel-sheet-column-title/

def convertToTitle(columnNumber):

    if(columnNumber <=26):
        return chr(65+(columnNumber-1))
    else:
        result=""
        while columnNumber :
            columnNumber-=1
            remender=(columnNumber)%26
            result=chr(65+remender)+result
            columnNumber=columnNumber//26
        return result


print(convertToTitle(28))