class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root and not root.left and root.right:
            return True
        
        stack = [root.left,root.right]

        while stack:
            curr1 = stack.pop()
            curr2 = stack.pop()
        
            if (curr1 and not curr2) or not curr1 and curr2:
                return False
            
            if not curr1 and not curr2:
                continue
            
            if curr1 and curr2:
                if curr1.val != curr2.val:
                    return False
         
            stack.append(curr1.left)
            stack.append(curr2.right)
            stack.append(curr1.right)
            stack.append(curr2.left)

        return True
