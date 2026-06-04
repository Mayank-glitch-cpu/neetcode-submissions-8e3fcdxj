class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj= [[] for _ in range(len(edges)+1)]

        def dfs(node, par):
            if node in visit:
                return True

            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei,node):
                    return True
            return False

        for u, v in edges:
            visit=set()
            adj[u].append(v)
            adj[v].append(u)
            if dfs(u,-1):
                return [u,v]
        return []