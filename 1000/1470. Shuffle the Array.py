class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        j = n
        res = []
        
        for i in range(0,n):
            res.append(nums[i])
            res.append(nums[j])
            j += 1
            
        return res
