# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        prev = dummy
        curr = head
        
        while curr and curr.next:
            
            #storing the next nodes
            other = curr.next.next
            second = curr.next
            
            #Altering the pointers
            second.next= curr
            curr.next = other
            prev.next = second
            
            #updating the pointers for next iteration
            prev = curr
            curr = other
            
        return dummy.next
        
