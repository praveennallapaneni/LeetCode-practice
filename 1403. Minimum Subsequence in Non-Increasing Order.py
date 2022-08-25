class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
        res = []
        s,g = 0,0
        l = len(nums)-1
        
        
        nums.sort()
        
        for i in range(len(nums)):
            s += nums[i]
        
        while s>=g:
            g += nums[l]
            s -= nums[l]
            res.append(nums[l])
            l -= 1
                 
        return res
