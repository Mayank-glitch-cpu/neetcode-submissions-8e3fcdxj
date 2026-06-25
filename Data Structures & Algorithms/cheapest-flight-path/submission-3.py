class Solution:
    # Dijkstra Algorithm
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]

        for s,d,p in flights:
            adj[s].append([d,p])

        dist= [float('inf')]*(n)
        q= deque()
        q.append((0,src,0))

        while q:
            stop, node, price= q.popleft()

            for dest, p in adj[node]:
                if (price + p)< dist[dest] and stop<=k:
                    dist[dest] = price + p
                    q.append((stop+1, dest, price+p))
        print(dist)
        return dist[dst] if dist[dst] != float('inf') else -1
