class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # brute force O(n^2)
        # length=0
        # area=0
        # out=[]
        # for i in range(len(heights)):
        #     for j in range(i,len(heights)):
        #         height= min(heights[i],heights[j])
        #         area=length*height
        #         out.append(area)
        #         length+=1
        #     length=0
        # print(out)
        # return max(out)

        # optimised with two pointers O(n)
        area= []
        head=0
        tail= len(heights)-1

        while head<tail:
            length= tail - head
            height= min(heights[head],heights[tail])
            water= length*height
            area.append(water)
            if heights[head]< heights[tail]:
                head+=1
            else:
                tail-=1
        print(area)
        return max(area)



            