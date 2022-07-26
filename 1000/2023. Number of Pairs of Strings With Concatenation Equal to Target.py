class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> list:
        
        res = 0
        temp = []
        for i in range(len(nums)):
            
            for j in range(0,len(nums)):
                
                if nums[i]+ nums[j] == target and i!=j:
                    res+=1
                    
        return res
