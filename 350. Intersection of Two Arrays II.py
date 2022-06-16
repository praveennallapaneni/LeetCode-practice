class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n in nums2:
            if n in nums1:
                res.append(n)
                nums1.remove(n)
        return res
 

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        numSet = Counter(nums1)
        result = []
        
        for num in nums2:
            if numSet[num] > 0:
                result.append(num)
                numSet[num] -= 1
        return result
