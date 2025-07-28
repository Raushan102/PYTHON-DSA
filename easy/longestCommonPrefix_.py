#https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs):
    i=0
    final_result=""
    current_resul=""

    if(len(strs)==1):
        return strs[0]

    while i< len(strs[0]):
        letter=strs[0][i]
        j=0
        while j < len(strs):
            if not(i < len(strs[j])):
                if(len(current_resul) > len(final_result)):
                    final_result=current_resul
                break
            elif strs[j][i]!=letter:
                if(len(current_resul) > len(final_result)):
                    final_result=current_resul
                break
            else:
                j+=1

        if(j>=len(strs)):
            current_resul+=strs[0][i]
            i+=1
        else:
            i+=1
    if(len(current_resul) > len(final_result)):
        final_result=current_resul
    return final_result



print(longestCommonPrefix(["flower","flow","flight"]))