#https://leetcode.com/problems/sorting-the-sentence/

def sortSentence( s):
    ArrayString = s.split(" ")  # convert string into array

    # Cyclic sort: place each word in its correct index
    i=0
    while i < len(ArrayString):
        temp = int(ArrayString[i][-1])  # get the number at end
        if temp != i + 1:
            j = temp - 1
            ArrayString[i], ArrayString[j] = ArrayString[j], ArrayString[i]
        else:
            i+=1

    # Remove the number from the end of each word
    for i in range(len(ArrayString)):
        word = ArrayString[i]
        ArrayString[i] = word[:-1]  # remove last character (the index)

    return ' '.join(ArrayString)


print(sortSentence("KTFkUVVrmYMSo2 wXlQraUqblfhCfDLK3 IfTuftYVualQ6 NhpQ5 HlRjClVtQrTFcwbx4 fi1"))