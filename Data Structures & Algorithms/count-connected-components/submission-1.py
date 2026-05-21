class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj= defaultdict(list)

        for edge in edges:
            u= edge[0]
            v= edge[1]
            adj[u].append(v)
            adj[v].append(u)
        
        visit= set()
        def dfs(node):
            if node not in visit:
                visit.add(node)
            for nei in adj[node]:   
                if nei not in visit:
                    visit.add(node)
                    dfs(nei)

        connected_nodes=0
        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                connected_nodes+=1
        return connected_nodes
            
        