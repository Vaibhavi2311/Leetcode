class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        list1=[]
        list2=[]
        for i in range(0,len(nums)):
            if nums[i]>0:
                list1.append(nums[i])
            elif nums[i]<0:
                list2.append(nums[i])
        for i in range(0,len(list1)):
            nums[2*i]=list1[i]
            nums[(2*i)+1]=list2[i]
        return nums
       