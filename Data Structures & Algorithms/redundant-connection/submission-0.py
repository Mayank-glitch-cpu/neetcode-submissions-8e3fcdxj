class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n= len(edges)
        adj= [[] for _ in range(n+1)]

        def dfs(node,par):
            if node in visit:
                return True

            visit.add(node)
            for nei in adj[node]:
                if nei==par:
                    continue
                if dfs(nei,node):
                    return True
            return  False

        
        for u,v in edges:
            visit=set()
            adj[u].append(v)
            adj[v].append(u)
            print(f"Trying to add edge: {u}-{v} -> Adjacency: {adj}")
            if dfs(u,-1):
                return [u,v]
        return []

            