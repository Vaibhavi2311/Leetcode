class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        left=0
        total_sum=sum(nums)
        for i in range(n):
            right=total_sum-left-nums[i]
            if left==right:
                return i
            else:
                left+=nums[i]
        return -1