class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1
        
        while l <= r:
            
            mid = l + (r-l)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                if nums[r] >= target and nums[r] < nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
            
            elif nums[mid] < target:
                if nums[l] <= target and nums[l] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
