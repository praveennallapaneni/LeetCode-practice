class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        res = 0
        stack = [root]
        if not root:
            return 0
        
        while stack:
            curr = stack.pop()
            res += 1

            if curr.left:
                stack.append(curr.left)
            
            if curr.right:
                stack.append(curr.right)
        
        return res
