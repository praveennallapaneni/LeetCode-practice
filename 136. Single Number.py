class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        map = {}

        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] += 1
            
            else:
                map[nums[i]] = 1
        
        for i in map:
            if map[i] == 1:
                return i
