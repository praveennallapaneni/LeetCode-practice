class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        
        prev = dummy
        curr = head
        
        for i in range(left-1):
            prev = curr
            curr = curr.next
            
        tail = None
        
        for i in range(right-left+1):
            tmp = curr.next
            curr.next = tail
            tail = curr
            curr = tmp
        
        prev.next.next = curr
        prev.next = tail
            
        return dummy.next
