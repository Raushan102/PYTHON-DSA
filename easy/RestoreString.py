#https://leetcode.com/problems/shuffle-string/description/

# frist way to swap in python

def restoreString(s,address):
 string=list(s)
 i=0
 while i < len(address):
  if address[i] != i:
   j = address[i]                     # keep the old value
   address[i], address[j] = address[j], address[i]   # real swap
   string[i],  string[j]  = string[j],  string[i]    # swap chars too
  else:
   i+=1
 return ''.join(string)

# second way to swap in python
def restoreString2(s,address):
 string=list(s)
 i=0
 while i < len(address):
  if address[i] != i:
   temp=address[i]
   strTemp=string[i]
   address[i]=address[temp]
   string[i]=string[temp]
   address[temp]=temp
   string[temp]=strTemp
  else:
   i+=1
 return "".join(string)



print(restoreString("codeleet",[4,5,6,7,0,2,1,3]))

print(restoreString2("codeleet",[4,5,6,7,0,2,1,3]))



