

def search(nums, target):
    start=0
    end=len(nums)-1
    while start <= end:
        mid=start+(end-start)//2
        if nums[mid] > target:
            end=mid-1
        elif nums[mid] < target:
            start=mid+1
        else:
            return mid

    return -1

arr=[1,2,3,4,5,6]

print(search(arr,3))








