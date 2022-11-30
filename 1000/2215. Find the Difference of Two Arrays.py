class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        res, temp1, temp2 = [], [], []

        for i in nums1:
            if i not in nums2:
                temp1.append(i)
        
        res.append(set(temp1))
        
        for i in nums2:
            if i not in nums1:
                temp2.append(i)
        
        res.append(set(temp2))

        return res
