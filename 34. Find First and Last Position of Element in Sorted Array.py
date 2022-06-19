class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        def leftIndex(nums,l,r, target):

            while l<r:
                mid = l + (r-l)//2

                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid-1]< target:
                    return mid
                else:
                    r = mid -1
            return l
    

        def rightIndex(nums,l,r, target):

            while l<r:
                mid = l + (r-l)//2

                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid+1]> target:
                    return mid
                else:
                    l = mid +1
            return r     
        
        l,r = 0, len(nums)-1
        
        
        while l<=r:
            mid = l + (r-l)//2
            
            if nums[mid] < target:
                l= mid +1
            elif nums[mid] > target:
                r = mid -1  
            else:
                return [leftIndex(nums,0,mid,target),rightIndex(nums,mid, len(nums)-1, target)]
            
        return [-1,-1]
