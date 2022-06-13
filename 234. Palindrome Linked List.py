class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        #Finding mid point ---  Slow pointer will be at Mid
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #Reversing the second half  --- slow will be at null and Prev will the last node
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left = head
        right = prev
        
        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        return True
