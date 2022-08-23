class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        right = prev
        left = head
        
        while right:
            temp1, temp2 = left.next, right.next
            left.next = right
            right.next = temp1
            left, right = temp1, temp2
        
