class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        maxSum = windowSum = sum(nums[:k])
        
        for i in range(0, len(nums)-k):
            
            windowSum += nums[i+k] - nums[i]
            maxSum = max(maxSum,windowSum)
              
        return float(maxSum/k)
