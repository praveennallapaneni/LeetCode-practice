class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        fast, slow = head,head
        res = 0
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left = head
        right = prev
        
        while left and right:
            temp = left.val + right.val
            res = max(res,temp)
            
            left = left.next
            right = right.next
        
        return res
