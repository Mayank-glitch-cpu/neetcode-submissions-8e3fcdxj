class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj= [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        print(adj)
        visit= set()
        def dfs(node):
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)

        connected=0
        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                connected+=1
        return connected