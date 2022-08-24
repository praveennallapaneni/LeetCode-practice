class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        left, right = head, head.next
        s = 0
        
        while right:
            
            # summation of integers stored in left pointer
            if right.val == 0:       
                left = left.next
                left.val = s
                s = 0
                
            else:
                s += right.val
            
            right = right.next
        
        left.next = None    # removing/deleting the link of the left pointer to rest of the list    
                               
        return head.next
