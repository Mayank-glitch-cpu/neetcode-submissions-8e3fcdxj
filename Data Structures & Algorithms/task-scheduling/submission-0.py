class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        task_map= {}
        q= deque()
        for task in tasks:
            if task in task_map:
                task_map[task]+=1
            else:
                task_map[task]=1
        
        max_heap= [-freq for freq in task_map.values()]
        heapq.heapify(max_heap)

        while max_heap or q:
            time+=1
            if max_heap:
                freq=heapq.heappop(max_heap)
                if freq+1<0:
                    q.append([freq+1,n+time])

            print('task',freq)
           
            if q and q[0][1] == time:
                heapq.heappush(max_heap,(q.popleft())[0])

        return time