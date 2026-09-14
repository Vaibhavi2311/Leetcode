class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''res=len(nums)

        for i in range(len(nums)):
            res+=(i-nums[i])
        return res'''
        n=len(nums)
        for i in range(0,n+1):
            if i not in nums:
                return i
