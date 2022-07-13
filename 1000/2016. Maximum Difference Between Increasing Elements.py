class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = 0
        l,r = 0,1
        
        while r < len(nums):
            diff = nums[r]-nums[l]
            if nums[l]<nums[r]:
                maxDiff = max(diff,maxDiff)
            else:
                l=r
            r+=1
        
        if maxDiff>0:
            return maxDiff
        else:
            return -1
