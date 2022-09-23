class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
        
        l,r = 0,0
        
        for i in nums:
            if i < target:
                l += 1
            
            if i == target:
                r += 1
                      
        return list(range(l, l+r))
