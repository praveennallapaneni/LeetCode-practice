class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy =  ListNode(None,head)
        prev = head
        curr = head.next
        
        while curr:
            
            if curr.val >= prev.val:
                prev = curr
                curr = curr.next
                continue
            
            temp = dummy
            while curr.val > temp.next.val:
                temp = temp.next
            
            prev.next = curr.next
            curr.next = temp.next
            temp.next = curr
            curr = prev.next
            
            
        return dummy.next
