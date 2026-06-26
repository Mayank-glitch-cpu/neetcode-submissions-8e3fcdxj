class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj= {c:set() for word in words for c in word}
        q= deque()

        # kahn's Algorithm
        def topoSort(N, adj, indegree):
            n= N
            topo=[]
            for char in indegree:
                if indegree[char]==0:
                    q.append(char)

            while q:
                char= q.popleft()
                topo.append(char)
                for nei in adj[char]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        q.append(nei)
            return ''.join(topo) if len(topo)==n else ''
        indegree= {c:0 for c in adj}

        # build the graph
        for i in range(len(words)-1):
            s1, s2 = words[i], words[i+1]

            # check for invalid prefix edges
            if len(s1)> len(s2) and s1[:len(s2)] == s2:
                return ""

            for j in range(min(len(s1),len(s2))):
                if s1[j]!=s2[j]:
                    if s2[j] not in adj[s1[j]]:
                        adj[s1[j]].add(s2[j])
                        indegree[s2[j]] += 1
                    break
        print('Indegree -->', indegree)
        print(adj)
        return topoSort(len(adj), adj, indegree)  