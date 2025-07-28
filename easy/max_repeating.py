#https://leetcode.com/problems/maximum-repeating-substring/

def maxRepeating(sequence, word):
    result=0
    i=0

    while i < len(sequence):
        j=0
        while j < len(word) and i < len(sequence):
            if word[j]==sequence[i]:
                i+=1
                j+=1
            else:
                j=0
                if word[j]==sequence[i]:
                    j+=1
                    i+=1
                else:
                    i+=1
        if j >= len(word):
            result+=1

    return result

print(maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba","aaaba"))