# https://leetcode.com/problems/minimum-time-difference/description/
class Solution(object):
    def findMinDifference(self, timePoints):
        
        result=0
        currentResult=0
        d=True
        i=0
        while i < len(timePoints):
             timeInMin=timeConverter(timePoints[i])
             timePoints[i]=timeInMin
             i+=1

        timePoints.sort()
        i=0
        while i < len(timePoints): 
             if i+1 < len(timePoints):
                  currentResult=abs(timePoints[i]-timePoints[i+1])

                  if d:
                      result=currentResult
                      d=False
                  if currentResult < result:
                       result=currentResult
             i+=1

        # circle difference after the mid night means next day 
        # that is many time left of present day + next day time 
        
        circleDifference=(1440 - timePoints[0])+timePoints[len(timePoints)-1]
        if circleDifference < result:
             result=circleDifference

        return result

               
                 
            

def timeConverter(str):
    tempArray=str.split(':')
    hours=int(tempArray[0])
    minute=int(tempArray[1])

    AllInMin=(hours*60)+minute

    if (AllInMin == 0):
           AllInMin=24*60
            
    return AllInMin

sol=Solution()

print(sol.findMinDifference(["02:15","21:10","02:15"]))
    
            
            
        