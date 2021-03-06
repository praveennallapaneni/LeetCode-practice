
#Iterative method

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        tmp = head
        
        while tmp and tmp.next:
            if tmp.next.val == tmp.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
            
        return head



# Recursive method

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        
        return self.deleteDuplicates(head.next)
