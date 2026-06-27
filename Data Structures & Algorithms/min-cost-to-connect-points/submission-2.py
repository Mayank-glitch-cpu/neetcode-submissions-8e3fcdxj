class DisjointSet():
    def __init__(self, n):
        self.par= [i for i in range(n)]
        self.rank= [0]*n
        # self.size= [0]*n

    def find(self, u):
        if self.par[u]!=u:
            self.par[u] = self.find(self.par[u])
        return self.par[u]

    def UnionByRank(self, u, v):
        pu, pv= self.find(u), self.find(v)
        if pu == pv:
            return False

        if self.rank[pu] > self.rank[pv]:
            self.par[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.par[pu] = pv
        else:
            self.par[pu] = pv
            self.rank[pu] +=1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n= len(points)
        dsu= DisjointSet(n)
        edges = []

        for i in range(n):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                dst= abs(xi - xj) + abs(yi - yj)
                edges.append((dst, i, j))

        edges.sort()
        res= 0

        for dst, u, v in edges:
            if dsu.UnionByRank(u, v):
                res+=dst
        return res
        