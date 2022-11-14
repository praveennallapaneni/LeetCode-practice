class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if not root:
                return None
            
            lTail = dfs(root.left)
            rTail = dfs(root.right)

            if lTail:
                lTail.right = root.right
                root.right = root.left
                root.left = None

            return rTail or lTail or root
        
        dfs(root)
