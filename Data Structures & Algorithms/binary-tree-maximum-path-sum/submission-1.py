# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath= -float('inf')
        def dfs(root):
            nonlocal maxPath
            if not root:
                return 

            left= self.getmax(root.left)
            right= self.getmax(root.right)
            maxPath= max(maxPath,left+right+root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return maxPath

    def getmax(self,root):
        if not root:
            return 0 

        left= self.getmax(root.left)
        right= self.getmax(root.right)
        path= max(left,right)+ root.val
        return max(0,path)


