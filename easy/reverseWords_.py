#https://leetcode.com/problems/reverse-words-in-a-string-iii/

def reverseWords(s):
    string_array=s.split(" ")

    for i in range(len(string_array)):
        words=list(string_array[i])
        k=0
        j=len(words)-1

        while(k<j):
            words[k],words[j]=words[j],words[k]
            k+=1
            j-=1
        temp="".join(words)
        string_array[i]=temp
    return " ".join(string_array)

print(reverseWords("Let's take LeetCode contest"))