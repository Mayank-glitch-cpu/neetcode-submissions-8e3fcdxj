class Solution:
    def trap(self, height: List[int]) -> int:
        left, right= 0, len(height) -1
        leftmost, rightmost = 0, 0
        trapped_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > leftmost:
                    leftmost= height[left]
                else:
                    trapped_water += leftmost - height[left]
                left +=1

            else:
                if rightmost < height[right]:
                    rightmost= height[right]
                else:
                    trapped_water += rightmost - height[right]
                right-=1
        return trapped_water