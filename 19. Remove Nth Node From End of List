# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        left = dummy # Adding dummy pointer so we can reach previous of the target node
        right = head
        
        # Marking the right pointer
        while n!=0 and right:
            
            right = right.next
            n-=1
        
        # Upading the pointers to identify the previous node of the target node
        
        while right:
            
            left = left.next
            right = right.next
        
        # Deleting the target node 
        left.next = left.next.next
        
        return dummy.next
            
