class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast, temp = head, head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                while temp!= fast:
                    temp = temp.next
                    fast = fast.next
                
                return temp
