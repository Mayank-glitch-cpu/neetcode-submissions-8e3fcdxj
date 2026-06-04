class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit= set()
        adj= defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            if node not in visit:
                visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
            
        connected_comp=0
        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                connected_comp+=1
        return connected_comp
                
