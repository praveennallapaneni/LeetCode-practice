# O(n) Time, O(1) space

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        curr = dummy
        
        while curr and curr.next:   
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next
