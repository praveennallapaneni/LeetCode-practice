class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] = nums[i] *nums[i]
            
        nums.sort()
        
        return nums


# Follow up: O(n)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        if nums[0]>=0:
            for i in range(len(nums)):
                nums[i] = nums[i]**2
            return nums
            
        l , r = 0, len(nums)-1  
        i = len(nums)-1
        
        new = [0]*(i+1)
        
        while l<=r:
            if abs(nums[l])<abs(nums[r]):
                new[i]= nums[r]**2
                r-=1
            
            else:
                new[i] = nums[l]**2
                l+=1           
            i-=1
        return new
