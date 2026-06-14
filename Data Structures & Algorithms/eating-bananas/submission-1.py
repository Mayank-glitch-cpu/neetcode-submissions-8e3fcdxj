class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowest_speed , highest_speed= 1, max(piles)
        res =0
        while lowest_speed <= highest_speed:
            test_speed = (lowest_speed + highest_speed) // 2
            total_time= 0
            for pile in piles:
                total_time += math.ceil(float(pile)/test_speed)

            if total_time <= h:
                res= test_speed
                highest_speed = test_speed - 1
            else:
                lowest_speed = test_speed +  1
        return res