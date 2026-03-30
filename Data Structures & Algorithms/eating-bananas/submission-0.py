import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k= max(piles)

        def canEat(piles,k):
            time =0
            for pile in piles:
                time += math.ceil(pile/k)
            return time

        def min_k(piles,start,end):
            if start==end:
                return start
            middle= (start+end)//2
            time= canEat(piles,middle)
            if time <= h:
                return min_k(piles,start,middle)

            else:
                return min_k(piles, middle+1,end)

        return min_k(piles,1,max_k)

            