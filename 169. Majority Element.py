class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        res, count = nums[0],1

        for i in range(1,len(nums)):
            if nums[i] == res:
                count += 1

            else:
                if count == 0:
                    res = nums[i]
                    count = 1
                
                count -= 1
        
        return res
