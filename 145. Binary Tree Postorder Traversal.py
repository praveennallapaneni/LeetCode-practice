class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res =[]
        stack = []

        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                res.append(curr.val)
                curr = curr.right
            
            temp = stack.pop()
            curr = temp.left

        return res[::-1]
