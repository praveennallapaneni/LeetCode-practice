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
    
    
    
 ## Binary Search Solution

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
        
        def leftIndex(nums,l,r,target):
            
            while l<r:
                mid = l + (r-l)//2
                
                if nums[mid] < target:
                    l = mid +1
                elif nums[mid-1] < target:
                    return mid
                else: 
                    r = mid-1
            return l
        
        def rightIndex(nums,l,r,target):
            
            while l<r:
                mid  = l + (r-l)//2
                
                if nums[mid]> target:
                    r = mid-1
                elif nums[mid+1]>target:
                    return mid
                else:
                    l = mid+1
            return r
        
        
        l,r = 0, len(nums)-1
        
        while l<=r:
            mid = l + (r-l)//2
            
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1                
            else:
                return list(range(leftIndex(nums,0,mid,target),rightIndex(nums,mid, len(nums)-1, target)+1))
                            
