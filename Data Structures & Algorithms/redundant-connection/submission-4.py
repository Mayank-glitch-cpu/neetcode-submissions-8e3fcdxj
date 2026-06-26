class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        q=deque()
        def bfs(node, par):
            q.append((node, par))
            while q:
                for i in range(len(q)):
                    node, par= q.popleft()
                    visit.add(node)

                    for nei in adj[node]:
                        if nei == par:
                            continue
                        elif nei in visit:
                            return True
                        else:
                            visit.add(nei)
                            q.append((nei,node))
            return False
            
        adj= [[] for i in range(len(edges)+1)]
        for u, v in edges:
            visit= set()
            adj[u].append(v)
            adj[v].append(u)
            if bfs(u,-1):
                return [u,v]
        return []
            

        