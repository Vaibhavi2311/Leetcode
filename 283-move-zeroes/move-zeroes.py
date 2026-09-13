class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''l=0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
        return nums'''
        n=len(nums)
        temp=[]
        for i in range(0,n):
           if nums[i]!=0:
                temp.append(nums[i])
        nz=len(temp)
        for i in range(0,nz):
            nums[i]=temp[i]
        for i in range(nz,n):
            nums[i]=0
        