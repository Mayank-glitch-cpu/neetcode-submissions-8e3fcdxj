class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea= 0
        stack = [] # monotoniacally increasing [index:height]

        for i , h in enumerate(heights):
            start= i

            while stack and stack[-1][1] > h:
                s_index, s_height = stack.pop()
                maxArea= max(maxArea, s_height*(i-s_index))
                start= s_index
            stack.append([start, h])

        while stack:
            s_index, s_height = stack.pop()
            maxArea= max(maxArea, s_height*(len(heights)-s_index))

        return maxArea