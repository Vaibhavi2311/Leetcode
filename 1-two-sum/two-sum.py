class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hashmap={}
        for i in range(0,n):
            remaining=target-nums[i]
            if remaining in hashmap:
                return [hashmap[remaining],i]
            hashmap[nums[i]]=i
        '''for i in range(0,n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]'''
