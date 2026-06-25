class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            curr = 0 
            time = 1
            for w in weights:
                curr+=w
                if curr> cap:
                    time+=1
                    curr = w
            print('It requires ',time,' days.')
            if time<=days:
                return True
            else:
                return False 

        l = max(weights)
        r = sum(weights)

        while l < r:
            m = (l+r)//2
            print("When cap is ",m)
            if canShip(m):
                r= m
            else:
                l = m+1
            print('l -->',l,'m -->',m,'r -->',r)
        return l