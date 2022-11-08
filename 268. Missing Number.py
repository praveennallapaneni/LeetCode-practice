class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        sum = int(l * (l+1)/2)
        for i in range(0,l):
            sum = sum - nums[i]
            
        return sum
        
