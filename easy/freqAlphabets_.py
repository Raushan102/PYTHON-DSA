
#https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
def freqAlphabets( s):
    string=list(s)
    result_string=""

    j=len(string)-1

    while j >=0 :
        if string[j]!="#":
            result_string=chr(97+(int(string[j]))-1)+result_string
            j-=1
        else:
            temp=string[j-1]
            temp=string[j-2]+temp
            result_string=chr(97+(int(temp))-1)+result_string
            j-=3
    return result_string



print(freqAlphabets("1326#"))