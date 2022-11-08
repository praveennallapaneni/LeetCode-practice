class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        res = []
        stack = []

        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr=  curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        ans = curr = TreeNode(res[0],None,None)

        for i in range(len(res)):
            curr.right = TreeNode(res[i])
            curr = curr.right
        
        return ans.right
