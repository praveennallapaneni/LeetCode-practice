class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        
        for i in range(len(nums)):
            first_number = nums[i]
            other_number = target - first_number
            
            #Identifying the second number
            for j in range(i + 1, len(nums)):
                second_number = nums[j]
                if second_number == other_number:
                    return [i, j]

                
#hashset solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        
        for i in range(len(nums)):
            if target-nums[i]in hashset:
                return [hashset[target-nums[i]],i]
            
            else:
                hashset[nums[i]]=i
