class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack= [] # this is going to hold prev index and height [i,h]
        maxArea= 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1]> h:
                startIndex, startHeight = stack.pop()
                maxArea= max(maxArea, startHeight * (i-startIndex))
                start = startIndex
            stack.append([start, h])

        for i, h in stack:
            maxArea= max(maxArea, h*(len(heights) - i))
        
        return maxArea