class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n=len(nums)
        low=0
        high=0
        while low<=high:
            mid=(low+high)//2
            if target not in nums:
                return -1
            for i in range(0,n):
                if nums[i]==target:
                    return i
                elif nums[i]<low:
                    high=mid-1
                else:
                    low=mid+1