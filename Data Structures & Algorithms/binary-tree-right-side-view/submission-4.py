# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out=[]
        if not root:
            return out
        q= deque()
        q.append(root)
        while q:
            node= q[0]
            out.append(node.val)
            print(out)
            for i in range(len(q)):
                nextNode=q.popleft()
                if nextNode.right:
                    q.append(nextNode.right)
                if nextNode.left:
                    q.append(nextNode.left)
        return out
