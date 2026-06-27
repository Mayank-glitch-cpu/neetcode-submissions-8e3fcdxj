class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}

        for  frm, to, p in flights:
            adj[frm].append([to,p])

        q= deque()
        dist= [float('inf')]*n
        dist[src]= 0
        q.append((0, src, 0)) # (stop, node, price)

        while q:
            stop, node, price = q.popleft()

            for nei, edge in adj[node]:
                if price + edge < dist[nei] and stop<=k:
                    dist[nei]= price + edge
                    q.append((stop+1, nei, price+ edge))

        return dist[dst] if dist[dst] != float('inf') else -1