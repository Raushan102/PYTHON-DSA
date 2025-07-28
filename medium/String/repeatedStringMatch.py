class Solution(object):
    def repeatedStringMatch(self, a, b):
        count=1
        
        if b in a:
            return count
        temp=a
        while len(temp) <= len(b):    
            if b not in temp:
                temp+=a
                count+=1
        if b in temp:
            return count
        temp+=a
        if b in temp:
            return count+1
        return -1

sol=Solution()
print(sol.repeatedStringMatch("abcd","cdabcdab"))