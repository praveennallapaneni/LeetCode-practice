# We are given access to the node that needs to be deleted. 
# So we are just deleting the next node and overwriting the existing node value with the next node

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
