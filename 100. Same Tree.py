class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if (not p and q) or (p and not q):
            return False
        
        queue1 = [p]
        queue2 = [q]

        while queue1 and queue2:
            curr1 = queue1.pop()
            curr2 = queue2.pop()

            if (not curr1 and curr2):
                return False
            
            if (curr1 and not curr2):
                return False
            
            if not curr1 and not curr2:
                continue
            
            if curr1 and curr2:
                if curr1.val != curr2.val:
                    return False

            queue1.append(curr1.left)
            queue1.append(curr1.right)
            queue2.append(curr2.left)
            queue2.append(curr2.right)
        
        return True
