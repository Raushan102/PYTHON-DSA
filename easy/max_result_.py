#https://leetcode.com/problems/jump-game-vi/



def max_result(nums, k):

        i=0
        result=nums[i]
        while i != len(nums)-1:

            j=1
            index=0
            max_sum=0
            while j <= k:

                if i+j < len(nums):
                    temp=nums[i]+nums[i+j]
                    if index==0 or max_sum < temp:
                        index=j+i
                        max_sum=temp
                        j+=1
                    else:
                        j+=1

                else:
                    i+=1
                    break

            i=index

            result+=nums[index]


        return result
print(max_result([100,-100,-300,-300,-300,-100,100],3))



