# https://leetcode.com/problems/determine-if-string-halves-are-alike/

def halvesAreAlike(s):
    division = len(s) // 2
    stringFirst = s[:division]


    stringSecond = s[division:]
    result_of_first_Str = 0
    result_of_second_Str = 0

    for i in range(len(stringFirst)):

      if stringFirst[i] in "aeiou" or stringFirst[i] in "AEIOU":
        result_of_first_Str += 1

      if stringSecond[i] in "aeiou" or stringSecond[i] in "AEIOU":
        result_of_second_Str += 1


    if result_of_second_Str == result_of_first_Str:
      return True
    else:
      return False


print(halvesAreAlike("textbook"))