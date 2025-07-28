#https://leetcode.com/problems/count-items-matching-a-rule/

def countMatches(items, ruleKey, ruleValue):
    searchIndex=0
    matches=0
    # set the mating index according to type because all the type are fix like type always comes at first and color at second and name at third
    if ruleKey=="color":
        searchIndex=1
    elif ruleKey=="name":
        searchIndex=2

    for item in range(len(items)):
        if items[item][searchIndex]==ruleValue:
            matches+=1
    return matches
items =[["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
print(countMatches(items,"name","iphone"))