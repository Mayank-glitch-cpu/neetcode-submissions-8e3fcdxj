class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res= [0]* len(temperatures)
        stack =[] # [i,t] where i is index and t is temeperature 

        for i, t in enumerate(temperatures):
            while stack and t> stack[-1][1]:
                stackInd, stackTemp= stack.pop()
                res[stackInd]=i-stackInd
            stack.append([i,t])
            print("Stack at Temp", t,' ',stack)
        return res