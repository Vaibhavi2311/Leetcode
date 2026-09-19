class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        count=0
        smaller=float("-inf")
        longest=0
        for i in range(0,n):
           num=nums[i]
           if num-1==smaller:
                count+=1
                smaller=num
           elif num!=smaller:
                count=1
                smaller=num
           longest=max(longest,count)
        return longest