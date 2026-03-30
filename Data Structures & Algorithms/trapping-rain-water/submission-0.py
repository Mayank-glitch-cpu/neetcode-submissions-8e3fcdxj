class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        leftmax=0
        rightmax=0
        trapped_water=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=leftmax:
                    leftmax=height[left]
                else:
                    trapped_water += leftmax- height[left]
                left+=1

            else:
                if height[right]>=rightmax:
                    rightmax= height[right]
                else:
                    trapped_water+= rightmax- height[right]
                right-=1
        return trapped_water