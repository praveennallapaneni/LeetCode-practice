class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        dummy = ListNode(None, list1)
        head = dummy
        
        prev = nxt = None

        for i in range(b+1):
            if i == a:
                prev = head

            head = head.next

        nxt = head.next
        prev.next = list2

        while list2.next:
            list2= list2.next

        list2.next = nxt

        return dummy.next    
