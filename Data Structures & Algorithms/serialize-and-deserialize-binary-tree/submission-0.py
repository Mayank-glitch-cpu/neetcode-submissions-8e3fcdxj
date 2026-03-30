# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.delimiter=","
        def dfs(root):
            if not root:
                return "N"+self.delimiter
            else:
                # self.string+=str(root.val) + self.delimiter
                return str(root.val)+self.delimiter+dfs(root.left)+ dfs(root.right)
        
        string=dfs(root)[:-1]
        print(string)
        return string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # first split the data based on a delimiter (',')
        splited= data.split(",")
        self.idx=0
        def dfs(data):
            if data[self.idx]=="N":
                self.idx+=1
                return None
            else:
                root=TreeNode(data[self.idx])
                self.idx+=1
            root.left= dfs(data)
            root.right= dfs(data)
            return root
        return dfs(splited)
