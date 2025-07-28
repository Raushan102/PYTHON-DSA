#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

def arrayStringsAreEqual(word1, word2):
    word1=''.join(word1)
    word2=''.join(word2)
    print(word1  , " " , word2 )

    if word1==word2:
        return True
    else:
        return False
word2=["a", "bc"]
word1=["ab", "c"]


print(arrayStringsAreEqual(word1,word2))