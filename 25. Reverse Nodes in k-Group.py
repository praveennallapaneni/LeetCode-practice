class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        
        groupPrev = dummy
        
        while True:
            kth = self.findKth(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next
            
            prev = kth.next
            curr = groupPrev.next
            
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
            
        return dummy.next
        
        
    def findKth(self, curr, k):
        while curr and k >0:
            curr = curr.next
            k -= 1
            
        return curr
