class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        nums = set(nums)
        res = 0
        flag = False # Initializing Flag to find if the previous value is in Nums
        
        while head:
            if head.val in nums:
                if not flag:
                    res += 1
                    flag = True
            else:
                flag = False
                
            head = head.next
                
        return res
