class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for n in nums2:
            if n in nums1:
                res.append(n)
        return set(res)
