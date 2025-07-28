class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        
        n1=len(sentence1)
        n2=len(sentence2)
        if(len(sentence2) == 1 or len(sentence1)==1):
            return sentence1[0]==sentence2[0] or sentence1[n1-1] == sentence2[n2-1]
        
        if(n1 > n2):
            word1=sentence1.split(" ")
            word2=sentence2.split(" ")
        else:
            word1=sentence2.split(" ")
            word2=sentence1.split(" ")
        
       
        k=0
        l=len(word2)-1
        i=0
        j=len(word1)-1

        while k <= l:
            if(word2[k]==word1[i]):
                k+=1
                i+=1
            elif (word2[l] == word1[j]):
                l-=1
                j-=1
            else:
                break
        return l < k


        

sol=Solution()
print("answer is ", sol.areSentencesSimilar("My name is Haley","My Haley"))

        
        