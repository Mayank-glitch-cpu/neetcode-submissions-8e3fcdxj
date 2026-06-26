class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n= numCourses
        # topo=[]
        adj = {i:[] for i in range(n)}
        indegree= [0]*n

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs]+=1
        # print(indegree)
        q= deque()

        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        cnt=0
        while q:
            crs= q.popleft()
            # topo.append(crs)
            cnt+=1
            for pre in adj[crs]:
                indegree[pre]-=1
                if indegree[pre]==0:
                    q.append(pre)
        # print(cnt)
        # print(topo)
        if cnt==n:
            return True
        else:
            return False
