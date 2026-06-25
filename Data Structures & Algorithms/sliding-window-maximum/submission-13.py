class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q= deque() # monotonically decreasing q
        out= []
        l, r = 0,0

        while r < len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()

            q.append(r)

            # remove from left of the window 
            # if number is out of bound of current window
            if l > q[0]:
                q.popleft()

            if (r+1)>=k:
                out.append(nums[q[0]])
                l+=1
            r+=1
        return out