
#https://leetcode.com/problems/defanging-an-ip-address/description/


def defangIPaddr(address):
    result=""
    for  x in address:
        if x==".":
            result+="[.]"
        else:
            result +=x
    return result




print(defangIPaddr("1.1.1.1"))