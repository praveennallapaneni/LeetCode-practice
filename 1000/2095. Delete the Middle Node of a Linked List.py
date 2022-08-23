class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(None,head)
        slow, fast = dummy, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = slow.next.next
        
        return dummy.next
