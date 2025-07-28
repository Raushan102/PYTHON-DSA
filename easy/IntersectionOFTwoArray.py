
def Intersection(nums1,nums2):
    intersection=[]
    for nums in nums2:
        if nums in nums1:
            intersection.append(nums)
            nums1.remove(nums)


    return intersection


nums=[1,2,2,3]
nums2=[3,2,2,5]
print(Intersection(nums,nums2))