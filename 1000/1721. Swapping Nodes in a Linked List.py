class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)

        prev, curr = dummy,dummy
        
        while k>0:
            curr = curr.next
            k -= 1
        
        kth = curr
    
        while curr:
            prev = prev.next
            curr = curr.next
            
        temp = prev.val
        prev.val = kth.val
        kth.val = temp
        
        return dummy.next
