"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_new= {}
        def dfs(curr_node):
            if curr_node in old_new:
                return old_new[curr_node]

            clone= Node(curr_node.val)
            old_new[curr_node]= clone

            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        return dfs(node)
