class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mapping= {pos:speed for pos, speed in zip(position,speed)}
        position.sort(reverse=True)
        print(position)
        print(mapping)
        stack=[]
        
        for pos in position:
            time = (target -pos)/mapping[pos]
            print('Time for car at pos ', pos, time)
            if not stack or time > stack[-1]:
                stack.append(time)
            print(stack)
        return len(stack)